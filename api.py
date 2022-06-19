from flask import Flask, request
import pandas as pd
import logging
from configparser import ConfigParser
from functools import reduce
import sys
from flask import Response
import json
from flask import jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import platform

class FlightSearchApi:

    def __init__(self, name):

        self.app = Flask(name)
        self.log = self.load_logger()
        self.config = self.load_config()
        self.h5_api_name = self.config.get('BASE', "h5_api_name")

        scheduler = BackgroundScheduler()
        scheduler.add_job(func=self.load_store, trigger="interval", seconds=2)
        scheduler.start()

        self.df_result = self.load_store()

        @self.app.route('/')
        def __index():
            return self.index()

        @self.app.route('/get_routes', methods=['GET'])
        def __get_routes():
            return self.get_routes()

    def index(self):
        return 'FlightSearchApi'

    def get_routes(self):
        return Response(json.dumps(self.df_result.to_dict(orient='records')), mimetype='application/json')

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

    def load_store(self):

        store = pd.HDFStore(self.h5_api_name)

        self.log.info('store loaded!')

        result_list = []

        for key in store.keys():
            df = store.get(key)
            df['RUN_KEY'] = str(key).replace('/', '')

            result_list.append(df)

        df_result = reduce(lambda left, right: pd.concat([left, right]), result_list)
        df_result = df_result.reset_index().drop('index', axis=1)

        df_result['DEP_DATE_0'] = df_result['DEP_DATE_0'].astype(str)
        df_result['ARR_DATE_0'] = df_result['ARR_DATE_0'].astype(str)
        df_result['DEP_DATE_1'] = df_result['DEP_DATE_1'].astype(str)
        df_result['ARR_DATE_1'] = df_result['ARR_DATE_1'].astype(str)

        df_result = df_result.sort_values('PRICE')

        return df_result

    def run(self, host, port):
        self.app.run(host=host, port=port)


def main():
    server = FlightSearchApi(__name__)
    server.run(host='0.0.0.0', port=9988)

if __name__ == '__main__':
    main()