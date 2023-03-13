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
import requests
from model.flight_result_model import *


class TequilaKiwi:

    def __init__(self):

        self.log = self.load_logger()
        self.config = self.load_config()

        self.date_from = self.config.get('BASE', "date_from")
        self.date_to = self.config.get('BASE', "date_from")
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
        self.api_key = self.config.get('BASE', 'api_key')

        now = datetime.now()
        self.time_key_to_file = now.strftime("%Y-%m-%d-%H-%M")

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

    def get_data_from_api(self):

        self.log.info('get_data_from_api started!')

        api = DefaultApi()

        airports_list = self.airports.split(',')

        flight_result = []

        for airport in airports_list:

            base_url = f'https://api.tequila.kiwi.com/v2/search?fly_from=BUD&curr=HUF' \
                       f'&fly_to={airport}' \
                       f'&date_from={self.date_from}' \
                       f'&date_to={self.date_to}' \
                       f'&nights_in_dst_from={self.nights_in_dst_from}' \
                       f'&nights_in_dst_to={self.nights_in_dst_to}' \
                       f'&flight_type=round' \
                       f'&adults={self.adults}' \
                       f'&children={self.children}' \
                       f'&infants={self.infants}' \
                       f'&adult_hold_bag={self.adult_hold_bag}' \
                       f'&adult_hand_bag={self.adult_hand_bag}' \
                       f'&max_stopovers={self.max_stopovers}' \

                #self.log.info(f'checking airport: {airport}')

            self.log.info(base_url)
            r = requests.get(url=base_url, headers={"apikey": self.api_key})
            data = r.json()

            self.log.info(data)

            flight_result = FlightResultModel.from_dict(data)

            self.log.debug(flight_result)


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

if __name__ == "__main__":

    flight_search = TequilaKiwi()
    flight_search.get_data_from_api()
    #file_to_attach_list = flight_search.evaluate_data()
    #flight_search.send_mail(file_to_attach_list)
    #flight_search.delete_old_xlsx()
