from typing import Dict

from pymongo import MongoClient

from config.configuration import Configuration


class MongoDb:
    __container: Dict[str, object] = {
        'app.configuration': None,
        'amqp.connection': None,
        'datasource.master.session': None,
        'service.complete_code_replication': None,
        'mongo.client': None,
    }

    def __init__(self):
        self.__init_app_configuration()
        self.__init_mongo_client()

    def __init_app_configuration(self):
        self.__container['app.configuration'] = self.__configuration = Configuration()

    def __init_mongo_client(self):
        host = self.__configuration.get('mongo.host')
        port = self.__configuration.get('mongo.port')
        max_pool_size = self.__configuration.get('mongo.max-pool-size')
        authSource = self.__configuration.get('mongo.db')
        collection = self.__configuration.get('mongo.collection')
        authMechanism = self.__configuration.get('mongo.authmechanism')
        username = self.__configuration.get('mongo.user')
        password = self.__configuration.get('mongo.password')

        try:
            # client = MongoClient(host=host, port=port, username=username, password=password, maxPoolSize=max_pool_size,
            #                      authMechanism=authMechanism, authSource=authSource)[
            #     authSource]
            client = MongoClient(host=host, port=port, username=username, password=password, maxPoolSize=max_pool_size,
                                 authSource=authSource)[authSource]

            self.__container['mongo.client'] = client[collection]
        except:
            raise Exception('Can not connect db')

    def get(self, key: str):
        value = self.__container.get(key)

        if value is None:
            raise Exception('Resource does not exist')

        return value
