import inspect
import sys
import os
from tables import NaturalNameWarning
import warnings
from model.flight_result_model import *
from sqlalchemy import create_engine, text
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
import numpy as np
import requests
from functools import reduce
from configparser import ConfigParser
import platform
import logging
import schedule
import time
import smtplib
from email.message import EmailMessage
import pymongo
from pymongo import MongoClient, UpdateOne
from bson.objectid import ObjectId
import concurrent.futures


class KiwiFlightMongoLoad:

    def __init__(self):

        self.log = self.load_logger()
        self.config = self.load_config()

        self.host = self.config.get('MONGO_DB', "host")
        self.port = self.config.get('MONGO_DB', "port")
        self.username = self.config.get('MONGO_DB', "username")
        self.password = self.config.get('MONGO_DB', "password")
        self.database_name = self.config.get('MONGO_DB', "database_name")
        self.api_key = self.config.get('BASE', "api_key")

        self.client, \
        self.search_result_collection, \
        self.airport_collection, \
        self.params_collection, self.final_result_collection = self.connect_to_mongo()
        self.load_new_data = self.config.get('BASE', "load_new_data")

    def load_config(self):
        try:
            self.log.info("Config file load begin")
            config = ConfigParser()
            if platform.platform()[:platform.platform().index('-')].lower() == 'macos':
                config_path = '/Users/kuligabor/Documents/KIWI/flight_search_py_be/kiwi.cfg'
            else:
                config_path = '/data/flight/flight_search_py_be/kiwi.cfg'
            config.read(config_path, encoding='utf-8')
            self.log.info("Config file load end")
            return config

        except Exception as e:
            self.log.error("Config file load error: {}".format(str(e)))
            sys.exit(1)

    def load_logger(self):
        try:
            log = logging.getLogger('LOG')
            log.setLevel(logging.DEBUG)
            fh = logging.FileHandler('mongo_flight_load.log', encoding="utf-8")
            fh.setLevel(logging.DEBUG)

            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)

            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
            ch.setFormatter(formatter)
            fh.setFormatter(formatter)

            log.addHandler(ch)
            log.addHandler(fh)
            log.info('Logger set')

            return log

        except Exception as e:
            print("logger error: " + str(e))
            sys.exit(1)

    def connect_to_mongo(self):
        self.log.debug('connect_to_mongo invoked!')
        client = MongoClient(self.host, int(self.port), username=self.username, password=self.password)
        db = client[self.database_name]

        search_result_collection = db['search_result']
        airport_collection = db['airports']
        params_collection = db['params']
        final_result_collection = db['final_result']

        self.log.debug('mongo connect success!')

        return client, search_result_collection, airport_collection, params_collection, final_result_collection

    def load_airports(self):
        self.log.debug('load_airports invoked.')
        airport_df = pd.DataFrame(list(self.airport_collection.find()))
        self.log.debug(f'airport_df loaded size: {len(airport_df)}')
        return airport_df

    def load_params(self):
        self.log.debug('load_params invoked.')
        param_filter = {
            'boolId': 1
        }
        params_df = pd.DataFrame(list(self.params_collection.find(param_filter)))
        self.log.debug(f'params_df loaded size: {len(params_df)}')
        return params_df

    def load_kiwi_data_thread(self, airport_df, params_df):
        self.log.debug('load_kiwi_data invoked')
        result_list_for_all_param = []

        all_airport_len = len(airport_df.loc[airport_df['COUNTRY'].isin(
            ['Italy', 'Spain', 'France', 'Greece'])])

        def fetch_data(airport, param, counter):
            base_url = f'https://api.tequila.kiwi.com/v2/search?fly_from={param["from_airport"]}&curr=HUF' \
                       f'&fly_to={airport["IATA"]}' \
                       f'&date_from={param["date_from"]}' \
                       f'&date_to={param["date_to"]}' \
                       f'&nights_in_dst_from={param["nights_in_dst_from"]}' \
                       f'&nights_in_dst_to={param["nights_in_dst_to"]}' \
                       f'&flight_type=round' \
                       f'&adults={param["adults"]}' \
                       f'&children={param["children"]}' \
                       f'&infants={param["infants"]}' \
                       f'&adult_hold_bag={param["adult_hold_bag"]}' \
                       f'&adult_hand_bag={param["adult_hand_bag"]}' \
                       f'&max_stopovers={param["max_stopovers"]}'

            self.log.debug(f' --search flight to: {airport["IATA"]} in {airport["COUNTRY"]} city {airport["CITY"]}')
            self.log.debug(
                f'Done percent: {round((counter / all_airport_len) * 100, 2)}% -> {counter} of {all_airport_len} handled!')

            try:
                r = requests.get(url=base_url, headers={"apikey": self.api_key})
                data = r.json()
                result_list_base = data['data']
            except Exception as e:
                self.log.debug(f'Error while getting flight data: {e}')
                return []

            result_list_final = []
            for result in result_list_base:
                mod_result = {}
                mod_result['searchId'] = result['id']
                mod_result['routeName'] = result['cityFrom'] + ' - ' + result['cityTo']
                result['crDate'] = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
                result['fxRate'] = result['conversion']['HUF'] / result['conversion']['EUR']
                result['boolId'] = 1
                result['paramRef'] = str(param["_id"])
                mod_result['resultList'] = [result]
                result_list_final.append(mod_result)

            return result_list_final

        counter = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            for _, param in params_df.iterrows():
                self.log.debug(f'Getting data for param: {param["_id"]} with executor: {executor}')
                for _, airport in airport_df.loc[
                    airport_df['COUNTRY'].isin(['Italy', 'Spain', 'France', 'Greece'])].iterrows():
                    counter = counter + 1
                    futures.append(executor.submit(fetch_data, airport, param, counter))

            for future in concurrent.futures.as_completed(futures):
                result_list_for_all_param.extend(future.result())

        return pd.DataFrame(result_list_for_all_param).drop_duplicates(subset=['searchId'])

    def load_kiwi_data(self, airport_df, params_df):
        self.log.debug('load_kiwi_data invoked.')
        result_list_for_all_param = []

        for _, param in params_df.iterrows():

            self.log.debug(f'Getting data for param: {param["_id"]}')
            result_list_base = []
            result_list_final = []

            '''for _, airport in airport_df.loc[airport_df['COUNTRY'].isin(
                    ['Italy', 'Spain', 'France', 'Greece'])].head(2).iterrows():'''
            all_airport_len = len(airport_df.loc[airport_df['COUNTRY'].isin(
                    ['Italy', 'Spain', 'France', 'Greece',
                     'Ireland', 'United Kingdom', 'Cyprus', 'Netherlands'])])
            counter = 0
            for _, airport in airport_df.loc[airport_df['COUNTRY'].isin(
                    ['Italy', 'Spain', 'France', 'Greece',
                     'Ireland', 'United Kingdom', 'Cyprus', 'Netherlands'])].iterrows():

                base_url = f'https://api.tequila.kiwi.com/v2/search?fly_from={param["from_airport"]}&curr=HUF' \
                           f'&fly_to={airport["IATA"]}' \
                           f'&date_from={param["date_from"]}' \
                           f'&date_to={param["date_to"]}' \
                           f'&nights_in_dst_from={param["nights_in_dst_from"]}' \
                           f'&nights_in_dst_to={param["nights_in_dst_to"]}' \
                           f'&flight_type=round' \
                           f'&adults={param["adults"]}' \
                           f'&children={param["children"]}' \
                           f'&infants={param["infants"]}' \
                           f'&adult_hold_bag={param["adult_hold_bag"]}' \
                           f'&adult_hand_bag={param["adult_hand_bag"]}' \
                           f'&max_stopovers={param["max_stopovers"]}'

                #self.log.debug(base_url)

                self.log.debug(f' --search flight to: {airport["IATA"]} in {airport["COUNTRY"]} city {airport["CITY"]}')


                try:
                    r = requests.get(url=base_url, headers={"apikey": self.api_key})
                    data = r.json()
                    self.log.debug(f'data len: {len(data["data"])}')
                    result_list_base.extend(data['data'])
                except Exception as e:
                    self.log.debug(f'Error while extending result_list: {e}')

                counter = counter + 1
                self.log.debug(f'Done percent: {round((counter / all_airport_len) * 100, 2)}%'
                               f' -> {counter} of {all_airport_len} handled!')

            for result in result_list_base:
                mod_result = {}
                mod_result['searchId'] = result['id']
                mod_result['routeName'] = result['cityFrom'] + '-' + result['cityTo']
                result['crDate'] = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
                result['modDate'] = ""
                result['fxRate'] = result['conversion']['HUF'] / result['conversion']['EUR']
                result['boolId'] = 1
                result['paramRef'] = str(param["_id"])
                result['children'] = param["children"]
                result['adults'] = param["adults"]
                result['adult_hold_bag'] = param["adult_hold_bag"]
                result['adult_hand_bag'] = param["adult_hand_bag"]
                mod_result['resultList'] = [result]
                result_list_final.append(mod_result)

            result_list_for_all_param.extend(result_list_final)

        return pd.DataFrame(result_list_for_all_param)

    def load_existing_search_result(self):
        self.log.debug('load_existing_search_result invoked.')
        existing_cursor = self.search_result_collection.find()
        self.log.debug('existing_cursor found!')
        existing_search_result_df = pd.DataFrame(list(existing_cursor))
        self.log.debug(f'existing_search_result_df len: {len(existing_search_result_df)}')
        return existing_search_result_df

    def transfer_define_old_and_existing_data(self, existing_search_result_df, new_search_result_df):
        self.log.debug('transfer_define_old_and_existing_data invoked!')
        old_new_merged_df = new_search_result_df.merge(existing_search_result_df,
                                                       on='searchId',
                                                       how='left',
                                                       suffixes=('_new', '_old'))

        search_result_to_load_df = old_new_merged_df.loc[
            old_new_merged_df['resultList_old'].isnull()].copy()

        search_result_to_update_df = old_new_merged_df.loc[
            old_new_merged_df['resultList_old'].notnull()].copy()

        self.log.debug(f'search_result_to_load_df size: {len(search_result_to_load_df)}')
        self.log.debug(f'search_result_to_update_df size: {len(search_result_to_update_df)}')

        def transfor_filter_price_change(x):
            new_price = x['resultList_new'][0]['price']
            old_price = x['resultList_old'][0]['price']
            if new_price == old_price:
                return 'same'
            else:
                return 'not_same'

        if len(search_result_to_update_df) > 0:
            search_result_to_update_df['price_changed'] = search_result_to_update_df.apply(transfor_filter_price_change,1)

            search_result_to_update_df = search_result_to_update_df.loc[
                search_result_to_update_df['price_changed'] == 'not_same'].copy()

            self.log.debug(f'search_result_to_update_df size after filter price not changed: '
                           f'{len(search_result_to_update_df)}')

        return search_result_to_load_df, search_result_to_update_df

    def export_to_load(self, search_result_to_load_df):
        self.log.debug('export_to_load invoked')

        try:
            search_result_to_load_df = search_result_to_load_df.rename(
                columns={'routeName_new': 'routeName',
                         'resultList_new': 'resultList'}).drop(['routeName_old',
                                                                'resultList_old',
                                                                '_id'], axis=1)
            self.log.debug('rename and drop done..')

        except Exception as e:
            self.log.debug('reanem not possible')

        self.log.debug('exporting search_result_to_load_df start!')
        self.search_result_collection.insert_many(search_result_to_load_df.to_dict(orient='records'))
        self.log.debug('exporting search_result_to_load_df done!')




    def export_update_existing(self, search_result_to_update_df):
        self.log.debug('export_update_existing invoked!')
        for _, v in search_result_to_update_df.iterrows():
            self.log.debug(f'Updating Object id: {v["_id"]}')

            document = self.search_result_collection.find({"_id": ObjectId(v['_id'])})

            if document:
                self.log.debug('Document found')
                update_operation = {
                    "$push": {
                        "resultList": {"$each": v['resultList_new']}
                    }
                }
                bool_set_operation = {"$set": {"resultList.$[].boolId": 0,
                                               "resultList.$[].modDate": datetime.now().strftime("%Y.%m.%d %H:%M:%S")}}

                self.search_result_collection.update_one(
                    {"_id": document[0]['_id']},
                    bool_set_operation)

                self.search_result_collection.update_one(
                    {"_id": document[0]['_id']},
                    update_operation)

                self.log.debug('update done!')
            else:
                self.log.debug('document not found!')

    def export_update_existing_batch_thread(self, df, batch_size=10, num_threads=1):
        def process_batch(batch):
            for document in batch:

                update_operation = {
                    "$push": {
                        "resultList": {"$each": document['resultList_new']}
                    }
                }
                bool_set_operation = {"$set": {"resultList.$[].boolId": 0,
                                               "resultList.$[].modDate": datetime.now().strftime("%Y.%m.%d %H:%M:%S")}}

                # Your existing code to modify the document in memory
                document["resultList"] = document["resultList"] + document['resultList_new']
                for item in document["resultList"]:
                    item["boolId"] = 0

                self.search_result_collection.bulk_write([
                    UpdateOne({"_id": document["_id"]}, [{"$set": document}])
                ])
                self.log.debug(f'Document updated: {document["_id"]}')

        all_size = len(df)
        counter = 0
        batch = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            for _, v in df.iterrows():
                document = self.search_result_collection.find_one({"_id": ObjectId(v['_id'])})
                if document:
                    batch.append(document)

                    if len(batch) >= batch_size:
                        self.log.debug('execute batch')
                        executor.submit(process_batch, list(batch))
                        batch = []

                    counter += 1
                    self.log.debug(
                        f'Done percent: {round((counter / all_size) * 100, 2)}% -> {counter} of {all_size} handled!')
                else:
                    self.log.error('document not found!')

        # Submit any remaining batch for processing
        try:
            # Attempt to shut down the executor
            executor.shutdown()
        except RuntimeError:
            pass
        if batch:
            process_batch(batch)

    def export_update_existing_batch(self, df, batch_size=100):
        batch = []
        all_size = len(df)
        counter = 0
        for _, v in df.iterrows():
            document = self.search_result_collection.find_one({"_id": ObjectId(v['_id'])})

            if document:
                update_operation = {
                    "$push": {
                        "resultList": {"$each": v['resultList_new']}
                    }
                }
                bool_set_operation = {"$set": {"resultList.$[].boolId": 0}}

                for item in document["resultList"]:
                    item["boolId"] = 0

                document["resultList"] = document["resultList"] + v['resultList_new']

                batch.append(document)
                batch_len = 0
                if len(batch) >= batch_size:
                    # Bulk update the batch
                    self.search_result_collection.bulk_write([
                        UpdateOne({"_id": d["_id"]}, [{"$set": d}]) for d in batch
                    ])
                    batch = []
                    batch_len = batch_len + batch_size
                    self.log.debug(f'{batch_len} document updated!')

                counter = counter + 1
                self.log.debug(f'Done percent: {round((counter / all_size) * 100, 2)}% -> {counter} of {all_size} handled!')
            else:
                self.log.error('document not found!')

        # Update any remaining documents
        if batch:
            self.search_result_collection.bulk_write([
                UpdateOne({"_id": d["_id"]}, [{"$set": d}]) for d in batch
            ])

    def load_final_result_aggregate(self):

        self.log.debug(f'load_final_result_aggregate invoked..')

        final_result_pipeline = [
                            {
                                '$unwind': {
                                    'path': '$resultList'
                                }
                            }, {
                                '$group': {
                                    '_id': {
                                        'searchId': '$searchId',
                                        'routeName': '$routeName'
                                    },
                                    'items': {
                                        '$push': {
                                            'searchId': '$searchId',
                                            'cityFrom': '$resultList.cityFrom',
                                            'cityTo': '$resultList.cityTo',
                                            'fxPrice': {
                                                '$round': '$resultList.conversion.EUR'
                                            },
                                            'start': {
                                                '$dateToString': {
                                                    'format': '%Y-%m-%d %H:%M',
                                                    'date': {
                                                        '$dateFromString': {
                                                            'dateString': '$resultList.local_departure',
                                                            'format': '%Y-%m-%dT%H:%M:%S.%LZ'
                                                        }
                                                    }
                                                }
                                            },
                                            'end': {
                                                '$dateToString': {
                                                    'format': '%Y-%m-%d %H:%M',
                                                    'date': {
                                                        '$dateFromString': {
                                                            'dateString': {
                                                                '$arrayElemAt': [
                                                                    '$resultList.route.local_departure', -1
                                                                ]
                                                            },
                                                            'format': '%Y-%m-%dT%H:%M:%S.%LZ'
                                                        }
                                                    }
                                                }
                                            },
                                            'days': {
                                                '$toString': '$resultList.nightsInDest'
                                            },
                                            'price': {
                                                '$round': '$resultList.price'
                                            },
                                            'flightNumber': {
                                                '$size': '$resultList.route'
                                            },
                                            'fxRate': {
                                                '$round': '$resultList.fxRate'
                                            },
                                            'crDate': '$resultList.crDate',
                                            'boolId': '$resultList.boolId',
                                            'deepLink': '$resultList.deep_link',
                                            'children': '$resultList.children',
                                            'adults': '$resultList.adults',
                                            'items': {
                                                '$map': {
                                                    'input': '$resultList.route',
                                                    'as': 'item',
                                                    'in': {
                                                        'text': {
                                                            '$concat': [
                                                                '$$item.cityFrom', ' - ', '$$item.cityTo', ' - ', {
                                                                    '$dateToString': {
                                                                        'format': '%Y-%m-%d %H:%M',
                                                                        'date': {
                                                                            '$dateFromString': {
                                                                                'dateString': '$$item.local_departure',
                                                                                'format': '%Y-%m-%dT%H:%M:%S.%LZ'
                                                                            }
                                                                        }
                                                                    }
                                                                }, ' - ', '$$item.airline'
                                                            ]
                                                        },
                                                        'flightNo': '$$item.flight_no'
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }, {
                                '$project': {
                                    '_id': 0,
                                    'searchId': '$_id.searchId',
                                    'text': '$_id.routeName',
                                    'items': 1
                                }
                            }, {
                                '$addFields': {
                                    'items': {
                                        '$map': {
                                            'input': {
                                                '$range': [
                                                    0, {
                                                        '$size': '$items'
                                                    }
                                                ]
                                            },
                                            'as': 'index',
                                            'in': {
                                                '$mergeObjects': [
                                                    {
                                                        '$arrayElemAt': [
                                                            '$items', '$$index'
                                                        ]
                                                    }, {
                                                        'isCheaper': {
                                                            '$cond': {
                                                                'if': {
                                                                    '$and': [
                                                                        {
                                                                            '$eq': [
                                                                                '$$index', {
                                                                                    '$subtract': [
                                                                                        {
                                                                                            '$size': '$items'
                                                                                        }, 1
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        }, {
                                                                            '$lt': [
                                                                                {
                                                                                    '$arrayElemAt': [
                                                                                        '$items.fxPrice', '$$index'
                                                                                    ]
                                                                                }, {
                                                                                    '$arrayElemAt': [
                                                                                        '$items.fxPrice', {
                                                                                            '$subtract': [
                                                                                                '$$index', 1
                                                                                            ]
                                                                                        }
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        }
                                                                    ]
                                                                },
                                                                'then': 1,
                                                                'else': 0
                                                            }
                                                        }
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                }
                            }, {
                                '$project': {
                                    'items': {
                                        '$filter': {
                                            'input': '$items',
                                            'as': 'item',
                                            'cond': {
                                                '$eq': [
                                                    '$$item.boolId', 1
                                                ]
                                            }
                                        }
                                    },
                                    'searchId': 1,
                                    'text': 1
                                }
                            }, {
                                '$sort': {
                                    'items.price': 1
                                }
                            }, {
                                '$group': {
                                    '_id': '$text',
                                    'items': {
                                        '$push': {
                                            'searchId': '$searchId',
                                            'cityFrom': '$cityFrom',
                                            'cityTo': '$cityTo',
                                            'fxPrice': '$fxPrice',
                                            'start': '$start',
                                            'end': '$end',
                                            'days': '$days',
                                            'price': '$price',
                                            'flightNumber': '$flightNumber',
                                            'fxRate': '$fxRate',
                                            'crDate': '$crDate',
                                            'boolId': '$boolId',
                                            'deepLink': '$deepLink',
                                            'isCheaper': '$isCheaper',
                                            'items': '$items'
                                        }
                                    }
                                }
                            }, {
                                '$addFields': {
                                    'text': '$_id',
                                    'items': '$items'
                                }
                            }, {
                                '$project': {
                                    '_id': 0,
                                    'text': 1,
                                    'items': 1
                                }
                            }, {
                                '$sort': {
                                    'items.items.price': 1
                                }
                            }
                        ]

        self.final_result_collection.delete_many({})

        search_result_cursor = self.search_result_collection.aggregate(final_result_pipeline, allowDiskUse=True)

        search_result = list(search_result_cursor)

        self.log.debug(f'search_result len: {len(search_result)}')

        if len(search_result) > 0:
            self.final_result_collection.insert_many(search_result)

        self.log.debug(f'load_final_result_aggregate done..')


    def send_mail(self, param_dict, file_to_attach_list=[]):

        self.log.info('send mail invoked with')

        msg = EmailMessage()
        my_address = self.config.get('MAIL', 'my_address')
        app_generated_password = self.config.get('MAIL', 'app_generated_password')

        now = datetime.now()
        time_key_to_run = now.strftime("%Y-%m-%d-%H-%M")

        msg["Subject"] = 'Fligh result - ' + time_key_to_run
        msg["From"] = my_address
        msg["To"] = self.config.get('MAIL', 'mail_to')

        message_text = self.config.get('MAIL', 'message_text')

        msg.set_content(f'{message_text}'
                        f' - param_dict: {str(param_dict)}')

        if len(file_to_attach_list) > 0:

            for file_name in file_to_attach_list:
                with open(file_name, "rb") as file:  # open image file
                    file_data = file.read()
                    msg.add_attachment(file_data, maintype="application", subtype="xlsx", filename=file_name)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(my_address, app_generated_password)  # login gmail account

            self.log.info("sending mail")
            smtp.send_message(msg)  # send message
            self.log.info("mail has sent")

    def main(self):

        self.log.debug('Main process start!')

        if self.load_new_data == '1':
            self.log.debug('new data loading enabled')
            airport_df = self.load_airports()
            params_df = self.load_params()

            new_search_result_df = self.load_kiwi_data(airport_df, params_df)
            existing_search_result_df = self.load_existing_search_result()

            if len(existing_search_result_df) > 0:
                search_result_to_load_df, \
                search_result_to_update_df = self.transfer_define_old_and_existing_data(existing_search_result_df,
                                                                                        new_search_result_df)
                self.export_to_load(search_result_to_load_df)
                #self.export_update_existing(search_result_to_update_df)
                if len(search_result_to_update_df) > 0:
                    self.export_update_existing_batch(search_result_to_update_df, 500)
            else:
                search_result_to_load_df = new_search_result_df
                self.export_to_load(search_result_to_load_df)

            self.send_mail(param_dict=params_df)

        else:
            self.log.debug('new data loading disabled')

        self.load_final_result_aggregate()

        self.log.debug('Main process finsihed!')

if __name__ == "__main__":

    #kiwi_flight_mongo_load = KiwiFlightMongoLoad()
    #kiwi_flight_mongo_load.main()

    try:
        flight_search = KiwiFlightMongoLoad()

        schedule.every().day.at("17:14").do(flight_search.main)
        #schedule.every().day.at("18:00").do(flight_search.main)

        while True:
            schedule.run_pending()
            time.sleep(1)

    except Exception as e:
        print('main exception :' + str(e))
        flight_search.send_mail(param_dict="ERROR: " + str(e))
        sys.exit(1)

