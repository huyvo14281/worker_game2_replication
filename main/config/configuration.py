import ast
import os
from os import environ

import yaml
from flatten_dict import flatten


class Configuration:
    __configuration = {
        'amqp.url': 'amqp://meete:p4ssw0rd@localhost:5672/meete',
        'amqp.connect_max_retries': 0,
        'log.level': 'INFO',
        'datasource.master.url': 'postgresql://meete:p4ssw0rd@localhost:5432/partner_voucher',
        'mongo.host': 'localhost',
        'mongo.port': 8081,
        'mongo.max-pool-size': '100',
        'mongo.db': 'meeteG',
        'mongo.collection': 'wheelBooking',
        'mongo.authmechanism': 'SCRAM-SHA-256',
        'mongo.user': 'huy',
        'mongo.password': '123'
    }

    def __init__(self):
        self.__parse_yaml()
        self.__parse_environ()

    def __parse_yaml(self):
        file_path = os.path.realpath(f'{os.path.dirname(__file__)}/../../application.yml')
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                configuration = yaml.load(file, Loader=yaml.FullLoader)
                if configuration is None:
                    configuration = {}

                def __dot_reducer(k1, k2):
                    if k1 is None:
                        return k2
                    else:
                        return k1 + '.' + k2

                configuration = flatten(configuration, reducer=__dot_reducer)
                configuration = {k: v for k, v in configuration.items() if k in self.__configuration}

                self.__configuration = {**self.__configuration, **configuration}

        except IOError:
            print('Cant find yaml configuration file in ' + file_path)
            return
        except Exception as ex:
            print(ex)

    def __parse_environ(self):
        def __to_environ_key(string: str):
            return string.upper().replace('.', '_')

        configuration = {
            key: ast.literal_eval((environ[environ_key]))
            for (key, environ_key) in [(key, __to_environ_key(key)) for key in self.__configuration]
            if environ_key in environ
        }

        self.__configuration = {**self.__configuration, **configuration}

    def __str__(self) -> str:
        return self.__configuration.__str__()

    def get(self, key):
        value = self.__configuration.get(key)

        if value is None:
            raise Exception('Invalid configuration information')

        return value
