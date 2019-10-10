from typing import Dict

from kombu import Connection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.configuration import Configuration
from service.ipos_order_created import IposOrderCreated
from service.merchant_voucher_completed_code import MerchantVoucherCompletedCode
from service.transaction_created import TransactionCreated


class Container:
    __container: Dict[str, object] = {
        'app.configuration': None,
        'amqp.connection': None,
        'datasource.master.session': None,
        'service.merchant_voucher_complete_code_replication': None,
        'service.ipos_order_created_replication': None,
        'service.transaction_created_replication': None,
        'mongo.client': None,
    }

    def __init__(self):
        self.__init_app_configuration()
        self.__init_amqp_connection()
        self.__init_datasource_master_session()
        self.__init_service_complete_code_replication()
        self.__init_service_ipos_order_created_replication()
        self.__init_service_transaction_created_replication()

    def __init_app_configuration(self):
        self.__container['app.configuration'] = self.__configuration = Configuration()

    def __init_amqp_connection(self):
        self.__container['amqp.connection'] = Connection(
            self.__configuration.get('amqp.url')
        )

    def __init_datasource_master_session(self):
        engine = create_engine(
            self.__configuration.get('datasource.master.url'),
            echo=True
        )
        self.__container['datasource.master.session_maker'] = sessionmaker(bind=engine)

    def __init_service_complete_code_replication(self):
        session_maker: sessionmaker = self.get('datasource.master.session_maker')
        self.__container['service.merchant_voucher_complete_code_replication'] = MerchantVoucherCompletedCode(
            session_maker
        )

    def __init_service_ipos_order_created_replication(self):
        session_maker: sessionmaker = self.get('datasource.master.session_maker')
        self.__container['service.ipos_order_created_replication'] = IposOrderCreated(
            session_maker
        )

    def __init_service_transaction_created_replication(self):
        session_maker: sessionmaker = self.get('datasource.master.session_maker')
        self.__container['service.transaction_created_replication'] = TransactionCreated(
            session_maker
        )

    def get(self, key: str):
        value = self.__container.get(key)

        if value is None:
            raise Exception('Resource does not exist')

        return value
