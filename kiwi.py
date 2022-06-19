import inspect
import sys
import os
from datetime import datetime
import pandas as pd
import time
from functools import reduce
import logging
from dateutil.relativedelta import relativedelta
from tables import NaturalNameWarning
import warnings
warnings.filterwarnings('ignore', category=NaturalNameWarning)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))
from swagger_client.api.default_api import DefaultApi
from configparser import ConfigParser
import smtplib
from email.message import EmailMessage
import shutil
import platform


class KiwiFlightChecker:

    def __init__(self):

        self.log = self.load_logger()
        self.config = self.load_config()

        self.depart_after = self.config.get('BASE', "depart_after")
        self.depart_before = self.config.get('BASE', "depart_before")
        self.nights_in_dst_from = self.config.get('BASE', "nights_in_dst_from")
        self.nights_in_dst_to = self.config.get('BASE', "nights_in_dst_to")
        self.max_stopovers = int(self.config.get('BASE', "max_stopovers"))
        self.adults = int(self.config.get('BASE', "adults"))
        self.children = int(self.config.get('BASE', "children"))
        self.infants = int(self.config.get('BASE', "infants"))
        self.adult_hold_bag = self.config.get('BASE', "adult_hold_bag")
        self.adult_hand_bag = self.config.get('BASE', "adult_hand_bag")
        self.child_hand_bag = self.config.get('BASE', "child_hand_bag")
        self.airports = self.config.get('BASE', "airports")
        self.h5_store_name = self.config.get('BASE', "h5_store_name")
        self.h5_api_name = self.config.get('BASE', "h5_api_name")
        self.result_dir = self.config.get('BASE', 'result_dir')

        now = datetime.now()
        self.time_key_to_file = now.strftime("%Y-%m-%d-%H-%M")

    def load_config(self):
        try:
            self.log.info("Config file load begin")
            config = ConfigParser()
            if platform.platform()[:platform.platform().index('-')].lower() == 'macos':
                config_path = '/Users/kuligabor/Documents/KIWI/kiwi_flight_search/kiwi.cfg'
            else:
                config_path = '/data/flight/kiwi.cfg'
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

    def get_data_from_api(self):

        self.log.info('get_data_from_api started!')

        api = DefaultApi()

        airports_list = self.airports.split(',')

        final_df_result_list = []

        for airport in airports_list:

            self.log.info(f'checking airport: {airport}')

            result = api.flights_get(partner='kulig1985kuligflight',
                                     fly_from='BUD',
                                     fly_to=airport,
                                     depart_after=self.depart_after,
                                     depart_before=self.depart_before,
                                     nights_in_dst_from=self.nights_in_dst_from,
                                     nights_in_dst_to=self.nights_in_dst_to,
                                     #flight_type='oneway',
                                     adults=self.adults,
                                     children=self.children,
                                     infants=self.infants,
                                     adult_hold_bag=self.adult_hold_bag,
                                     adult_hand_bag=self.adult_hand_bag,
                                     child_hand_bag=self.child_hand_bag,
                                     curr='HUF',
                                     max_stopovers=self.max_stopovers)

            self.log.info(f'{result.search_id} done!')

            #with open('debug_result/' + str(result.search_id) + '.json', 'w') as outfile:
            #    json.dump(result.to_dict(), outfile)

            if len(result.data) > 0:

                result_list = []

                for itinerary in result.data:

                    #print(itinerary.id)
                    #print(itinerary)

                    #with open('debug_result/' + str(itinerary.id) + '.json', 'w') as outfile:
                    #    json.dump(itinerary.to_dict(), outfile)

                    result_dict = {}

                    result_dict['ID'] = itinerary.id
                    result_dict['PRICE'] = itinerary.price
                    result_dict['FLY_DURATION'] = itinerary.fly_duration
                    result_dict['RET_DURATION'] = itinerary.return_duration

                    return_type = 0

                    for segment in itinerary.route:

                        #print(segment)
                        #return_type = str(segment.id)

                        result_dict['ID_' + str(return_type)] = segment.id
                        result_dict['DEP_DATE_' + str(return_type)] = datetime.fromtimestamp(segment.d_time)
                        result_dict['ARR_DATE_' + str(return_type)] = datetime.fromtimestamp(segment.a_time)

                        result_dict['DEP_DATE_' + str(return_type)] = datetime.fromtimestamp(segment.d_time)
                        result_dict['ARR_DATE_' + str(return_type)] = datetime.fromtimestamp(segment.a_time)

                        result_dict['AIRLINE_' + str(return_type)] = segment.airline
                        result_dict['CITY_FROM_' + str(return_type)] = segment.city_from
                        result_dict['CITY_TO_' + str(return_type)] = segment.city_to
                        result_dict['FLIGHT_NO_' + str(return_type)] = segment.flight_no

                        return_type = return_type + 1

                    result_list.append(result_dict)
                    #print(result_dict)

                #print(result_list)

                df = pd.DataFrame(result_list)
                df['PRICE'] = df['PRICE'].astype(int)

                self.log.info(f'Result dataframe len: {len(df)}')
                final_df_result_list.append(df)
                self.log.info('---------***--***---------')

            else:
                self.log.info('Response is empty!')

        final_result = reduce(lambda left, right: pd.concat([left, right]), final_df_result_list)

        self.log.info(f'final_result dataframe len: {len(final_result)}')

        final_result = final_result.loc[final_result['PRICE'] <= int(self.config.get('BASE', 'price_limit'))]

        self.log.info(f'final_result dataframe len after remove > price limit {len(final_result)}')

        if self.config.get('BASE', 'save_actual_run_to_excel') == '1':
            final_result.to_excel(self.result_dir + 'final_result_API_CALL_' + self.time_key_to_file + '.xlsx', index=False)

        store = pd.HDFStore(self.h5_store_name)
        store.append(self.time_key_to_file, final_result)

        shutil.copy(self.h5_store_name, self.h5_api_name)

        self.log.info(f'Final result saved to {self.h5_store_name} on time_key: {self.time_key_to_file}')

        self.log.info('Skypicker api call ended!')

    def evaluate_data(self):

        self.log.info('Start evaluation of stored data!')

        store = pd.HDFStore(self.h5_store_name)

        self.log.info('store loaded!')

        result_list = []
        file_to_attach_list = []

        for key in store.keys():
            df = store.get(key)
            df['RUN_KEY'] = str(key).replace('/', '')

            result_list.append(df)

        df_result = reduce(lambda left, right: pd.concat([left, right]), result_list)
        df_result = df_result.reset_index().drop('index', axis=1)

        self.log.info(f'Full saved df_result size: {len(df_result)}')

        df_result['RUN_DATE'] = pd.to_datetime(df_result['RUN_KEY'], format='%Y-%m-%d-%H-%M')

        last_need_days = int(self.config.get('BASE', 'last_need_days'))
        self.log.info(f'param_days: {last_need_days}')
        last_need_date = (pd.to_datetime(datetime.now() + relativedelta(days=int(last_need_days)))).strftime("%Y-%m-%d")

        df_result = df_result.loc[df_result['RUN_DATE'] > last_need_date].copy()

        self.log.info(f'df_result size after drop not needed days: {len(df_result)}')

        df_result = df_result.sort_values(['ID', 'RUN_KEY'])
        df_result['diffs'] = df_result['PRICE'].diff()
        mask = df_result['ID'] != df_result['ID'].shift(1)
        df_result.loc[mask, 'diffs'] = 0

        df_result['EXECUTE_ORDER'] = df_result.groupby(['ID']).cumcount()

        self.log.info('Diffs and execute order done!')

        df_sum_dif = df_result[['ID', 'diffs']].groupby('ID').sum().reset_index()
        df_sum_dif = df_sum_dif.rename(columns={'diffs': 'SUM_DIFF'})
        df_result = pd.merge(df_result, df_sum_dif, how='left', on='ID')

        self.log.info('SUM Diffs calculation DONE!')

        last_run_result_df = df_result.loc[df_result.groupby(['ID'])['EXECUTE_ORDER'].idxmax()]
        last_run_result_df = last_run_result_df.sort_values('PRICE')

        self.log.info(f'last_run_result_df len: {len(last_run_result_df)}')

        file_name_last_run = self.result_dir + 'last_run_result_df_' + self.time_key_to_file + '.xlsx'
        last_run_result_df[[
                            'RUN_KEY',
                            'ID',
                            'CITY_FROM_0',
                            'CITY_TO_0',
                            'DEP_DATE_0',
                            'AIRLINE_0',
                            'FLIGHT_NO_0',
                            'CITY_FROM_1',
                            'CITY_TO_1',
                            'DEP_DATE_1',
                            'AIRLINE_1',
                            'FLIGHT_NO_1',
                            'FLY_DURATION',
                            'PRICE',
                            'SUM_DIFF']].to_excel(file_name_last_run, index=False)

        self.log.info(f'last_run_result_df saved as: {file_name_last_run}')
        file_to_attach_list.append(file_name_last_run)

        diff_th = int(self.config.get('BASE', 'diff_th'))
        sum_diff_th = int(self.config.get('BASE', 'sum_diff_th'))

        self.log.info(f'diff_th: {diff_th} sum_diff_th: {sum_diff_th}')

        heads_up_id_list = list(last_run_result_df.loc[(last_run_result_df['diffs'] < diff_th) &
                            (last_run_result_df['SUM_DIFF'] < sum_diff_th), 'ID'].values)

        if len(heads_up_id_list) > 0:

            self.log.info(f'Found {len(heads_up_id_list)} routes that should be checked!')
            routes_to_check_df = df_result.loc[df_result['ID'].isin(heads_up_id_list)]
            file_name_route_check = self.result_dir + 'routes_to_check_df_' + self.time_key_to_file + '.xlsx'
            routes_to_check_df[[
                            'ID',
                            'CITY_FROM_0',
                            'CITY_TO_0',
                            'DEP_DATE_0',
                            'AIRLINE_0',
                            'FLIGHT_NO_0',
                            'CITY_FROM_1',
                            'CITY_TO_1',
                            'DEP_DATE_1',
                            'AIRLINE_1',
                            'FLIGHT_NO_1',
                            'FLY_DURATION',
                            'PRICE',
                            'SUM_DIFF']].to_excel(file_name_route_check, index=False)
            self.log.info(f'routes_to_check_df saved as: {file_name_route_check}')
            file_to_attach_list.append(file_name_route_check)

        else:
            self.log.info('No routes found to check send actual result!')

        return file_to_attach_list

    def send_mail(self, file_to_attach_list=[]):

        self.log.info('send mail invoked with')

        msg = EmailMessage()
        my_address = self.config.get('MAIL', 'my_address')
        app_generated_password = self.config.get('MAIL', 'app_generated_password')

        msg["Subject"] = 'Fligh result - ' + self.time_key_to_file
        msg["From"] = my_address
        msg["To"] = self.config.get('MAIL', 'mail_to')

        message_text = self.config.get('MAIL', 'message_text')

        msg.set_content(f'{message_text}'
                        f' - adults: {self.adults} '
                        f' - children: {self.children} '
                        f' - infant: {self.infants} '
                        f' - adult_hold_bag: {self.adult_hold_bag} '
                        f' - adult_hold_bag: {self.adult_hand_bag} '
                        f' - child_hand_bag: {self.child_hand_bag} '
                        f' - depart_after: {self.depart_after} '
                        f' - depart_before: {self.depart_before} '
                        f' - nights_in_dst_from: {self.nights_in_dst_from} '
                        f' - nights_in_dst_to: {self.nights_in_dst_to} '
                        f'-  max_stopovers: {self.max_stopovers}')

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

    def delete_old_xlsx(self):

        path = self.result_dir
        now = time.time()

        self.log.info('Delete old files!')

        for f in os.listdir(path):
            f = os.path.join(path, f)
            if (os.stat(f).st_mtime < now - 3 * 86400) & (os.path.isfile(f)) & f.endswith('.xlsx'):
                self.log.info(f'{f} eligible to delete!')
                os.remove(f)
            else:
                self.log.info(f'{f} is NOT eligible to delete!')

if __name__ == "__main__":

    flight_search = KiwiFlightChecker()

    flight_search.get_data_from_api()
    file_to_attach_list = flight_search.evaluate_data()
    flight_search.send_mail(file_to_attach_list)
    flight_search.delete_old_xlsx()



