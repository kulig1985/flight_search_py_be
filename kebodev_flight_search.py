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

warnings.filterwarnings('ignore', category=NaturalNameWarning)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))


class KebodevFlightSearch:

    def __init__(self):

        self.log = self.load_logger()
        self.config = self.load_config()

        self.api_key = self.config.get('BASE', 'api_key')
        self.db_user = self.config.get('DB', "db_user")
        self.db_pass = self.config.get('DB', "db_pass")
        self.db_host = self.config.get('DB', "db_host")
        self.db_port = self.config.get('DB', "db_port")
        self.database = self.config.get('DB', "database")

        self.connection = self.create_db_connect()
        self.session = self.create_db_session()

        now = datetime.now()

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
            fh = logging.FileHandler('fligh_runner.log', encoding="utf-8")
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

    def create_db_connect(self):

        connect_string = 'mysql+pymysql://' + self.db_user + \
                         ":" + self.db_pass + "@" + self.db_host + ":" + \
                         self.db_port + "/" + self.database

        #self.log.debug(connect_string)

        connection = create_engine(connect_string,
                                   pool_pre_ping=True,
                                   connect_args={'connect_timeout': 6000}).connect()

        self.log.debug("db connect success!")

        return connection

    def create_db_session(self):

        Session = sessionmaker(bind=self.connection)
        session = Session()

        return session

    def create_flight_search_instance(self, fsre_id):

        Base = declarative_base()

        class FlightSearchInstance(Base):
            __tablename__ = 'FLIGHT_SEARCH_INSTANCE'
            FSIN_ID = Column(Integer, primary_key=True)
            FSRE_ID = Column(Integer)
            MOD_DATE = Column(DateTime)
            STAT_ID = Column(Integer)

        new_flight_search_instance = FlightSearchInstance(FSRE_ID=fsre_id, STAT_ID=0)
        self.session.add(new_flight_search_instance)
        self.session.commit()

        return new_flight_search_instance

    def read_all_fligh_request(self):

        flight_req_sql = self.config.get('SQL', "flight_req_sql")
        flight_req_df = pd.read_sql(text(flight_req_sql), self.connection)
        self.log.debug(f'flight_req_df len: {len(flight_req_df)}')

        return flight_req_df

    def get_data_from_api(self, param_dict, airports_list):

        self.log.info('get_data_from_api started!')

        flight_result_list = []
        error_list = []

        counter = 1

        for airport in airports_list:

            try:

                self.check_airport(airport, airports_list, counter, error_list, flight_result_list, param_dict)
                counter = counter + 1

            except Exception as e:

                self.log.error(f"Exception: {e} at aiport: {airport} wait 3 sec and continoue!")
                time.sleep(3)

        final_result = reduce(lambda left, right: pd.concat([left, right]), flight_result_list)

        if len(final_result) > 0:
            final_result['FSIN_ID'] = param_dict['fsin_id']
            final_result.sort_values('PRICE', inplace=True)
            final_result.reset_index(inplace=True, drop=True)
            final_result['DEP_DATE_OUT'] = final_result['DEP_DATE_OUT'].dt.strftime('%Y-%m-%d %H:%M')
            final_result['ARR_DATE_OUT'] = final_result['ARR_DATE_OUT'].dt.strftime('%Y-%m-%d %H:%M')
            final_result['DEP_DATE_BACK'] = final_result['DEP_DATE_BACK'].dt.strftime('%Y-%m-%d %H:%M')
            final_result['ARR_DATE_BACK'] = final_result['ARR_DATE_BACK'].dt.strftime('%Y-%m-%d %H:%M')
            final_result.drop_duplicates(subset=['ID'], inplace=True)

            self.log.debug(f'final_result len: {len(final_result)}')

            final_result.to_sql('FLIGHT_SEARCH_RESULT', self.connection, if_exists='append', index=False)

            return error_list

    def check_airport(self, airport, airports_list, counter, error_list, flight_result_list, param_dict):
        self.log.debug(f'Checking {counter} of {len(airports_list)} - {param_dict["dep_airport"]} to {airport}')

        error_dict = {}
        base_url = f'https://api.tequila.kiwi.com/v2/search?fly_from={param_dict["dep_airport"]}&curr=HUF' \
                   f'&fly_to={airport}' \
                   f'&date_from={param_dict["date_from"]}' \
                   f'&date_to={param_dict["date_to"]}' \
                   f'&nights_in_dst_from={param_dict["nights_in_dst_from"]}' \
                   f'&nights_in_dst_to={param_dict["nights_in_dst_to"]}' \
                   f'&flight_type=round' \
                   f'&adults={param_dict["adults"]}' \
                   f'&children={param_dict["children"]}' \
                   f'&infants={param_dict["infants"]}' \
                   f'&adult_hold_bag={param_dict["adult_hold_bag"]}' \
                   f'&adult_hand_bag={param_dict["adult_hand_bag"]}' \
                   f'&max_stopovers={param_dict["max_stopovers"]}'
        self.log.debug(base_url)
        time.sleep(1)
        r = requests.get(url=base_url, headers={"apikey": self.api_key})
        # self.log.debug(r.text)
        data = r.json()
        # self.log.debug(f'statuscode: {r.status_code}')
        if r.status_code == 200:

            try:
                flight_result = FlightResultModel.from_dict(data)

                # self.log.debug(len(flight_result.data))

                if len(flight_result.data) > 0:

                    result_list = []

                    for data in flight_result.data:

                        result_dict = {}

                        result_dict['FX_RATE'] = flight_result.fx_rate
                        result_dict['ID'] = data.id
                        result_dict['PRICE'] = data.price
                        result_dict['EUR_PRICE'] = np.round(data.price / flight_result.fx_rate, 2)
                        result_dict['FLY_DURATION'] = np.round(int(data.duration.departure) / 3600, 2)
                        result_dict['RET_DURATION'] = np.round(int(data.duration.duration_return) / 3600, 2)
                        result_dict['TOTAL_DURATION'] = np.round(int(data.duration.total) / 3600, 2)

                        return_type = 0
                        col_suffix = 'OUT'

                        for route in data.route:

                            if return_type == 1:
                                col_suffix = 'BACK'

                            result_dict['ID_' + str(col_suffix)] = route.id
                            result_dict['DEP_DATE_' + str(col_suffix)] = route.local_departure
                            result_dict['ARR_DATE_' + str(col_suffix)] = route.local_arrival

                            result_dict['AIRLINE_' + str(col_suffix)] = route.airline
                            result_dict['CITY_FROM_' + str(col_suffix)] = route.city_from
                            result_dict['COUNTRY_FROM_' + str(col_suffix)] = data.country_from.name
                            result_dict['COUNTRY_TO_' + str(col_suffix)] = data.country_to.name
                            result_dict['CITY_TO_' + str(col_suffix)] = route.city_to
                            result_dict['FLIGHT_NO_' + str(col_suffix)] = route.flight_no

                            return_type = return_type + 1

                        result_list.append(result_dict)
                        # log.debug(result_dict)

                    df = pd.DataFrame(result_list)
                    df['PRICE'] = df['PRICE'].astype(int)

                    self.log.debug(f'Result dataframe len: {len(df)}')
                    flight_result_list.append(df)

                else:
                    self.log.debug('no routes found!')

            except Exception as e:
                self.log.error('json parse error:' + str(e))
                error_dict['flyTo'] = airport
                error_dict['fsin_id'] = param_dict['fsin_id']
                error_list.append(error_dict)

        else:
            self.log.debug("response not 200")
            error_dict['flyTo'] = airport
            error_dict['fsin_id'] = param_dict['fsin_id']
            error_list.append(error_dict)

    def save_error(self, error_list):

        self.log.debug('save_error invoked!')
        error_df = pd.DataFrame(error_list).rename(columns={'flyTo': 'FLY_TO', 'fsin_id': 'FSIN_ID'})

        self.log.debug(f'error_df list size: {len(error_df)}')

        error_df.to_sql('FLIGHT_SEARCH_ERROR', self.connection, if_exists='append', index=False)

        self.log.debug('Error info saved!')

    def main(self):


        flight_req_df = self.read_all_fligh_request()

        self.log.debug(f'flight_req_df len: {len(flight_req_df)}')

        for k, v in flight_req_df.iterrows():
            fsre_id = v['FSRE_ID']

            param_dict = {'dep_airport': v['DEP_AIRPORT'], 'date_from': v['DATE_FROM'], 'date_to': v['DATE_TO'],
                          'nights_in_dst_from': v['NIGH_IN_DEST_FROM'], 'nights_in_dst_to': v['NIGH_IN_DEST_TO'],
                          'max_stopovers': int(v['MAX_STOP_OVERS']), 'adults': int(v['ADULTS']),
                          'children': int(v['CHILDREN']), 'infants': int(v['INFANTS']), 'adult_hold_bag': v['ADULT_HOLD_BAG'],
                          'adult_hand_bag': v['ADULT_HAND_BAG'], 'child_hand_bag': v['CHILD_HAND_BAG']}

            self.log.debug(f'START processing fsre_id: {fsre_id} NAME: {v["SEARCH_NAME"]} - PARAMS -> {param_dict}')

            #airport_list_sql = self.config.get('SQL', "airport_list_sql").format(fsre_id=v['FSRE_ID'])
            #airport_list_df = pd.read_sql(airport_list_sql, self.connection)

            try:

                new_flight_search_instance = self.create_flight_search_instance(fsre_id=fsre_id)
                param_dict['fsin_id'] = new_flight_search_instance.FSIN_ID

                error_list = self.get_data_from_api(param_dict=param_dict, airports_list=flight_req_df['IATA'].values[0].split(','))

                self.log.debug(f'error_list: {error_list}')

                self.save_error(error_list)

                new_flight_search_instance.MOD_DATE = datetime.now()
                new_flight_search_instance.STAT_ID = 1
                self.session.merge(new_flight_search_instance)
                self.session.commit()

                self.log.debug(f'FINISHED processing fsre_id: {fsre_id}')

                self.log.debug('Sending email!')

                self.send_mail(param_dict=param_dict)

                self.log.debug('Sending email Done!')
                self.log.debug('Exiting!')

            except Exception as e:

                self.log.error(f'Main exception: {e}')

                new_flight_search_instance.MOD_DATE = datetime.now()
                new_flight_search_instance.STAT_ID = -1
                self.session.merge(new_flight_search_instance)
                self.session.commit()
                sys.exit(1)


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


if __name__ == "__main__":

    try:
        flight_search = KebodevFlightSearch()

        schedule.every().day.at("10:18").do(flight_search.main)
        schedule.every().day.at("18:00").do(flight_search.main)

        while True:
            schedule.run_pending()
            time.sleep(1)

    except Exception as e:
        print('main exception :' + str(e))
        sys.exit(1)

