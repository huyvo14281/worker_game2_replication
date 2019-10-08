import sys

from config.configuration import Configuration
from config.container import Container
from config.registry import Registry
from listener.merchant_voucher_code_completed_listener import *
from listener.ipos_order_created_listener import *
from listener.transaction_created_listener import *


class Application:
    def __init__(self):
        self.container = Container()
        self.app_configuration: Configuration = self.container.get('app.configuration')
        self.__set_log_level()
        pass

    def start(self):
        connect_max_retries: int = self.app_configuration.get('amqp.connect_max_retries')
        with self.container.get('amqp.connection') as conn:
            registry = Registry(conn, connect_max_retries)
            merchant_voucher_complete_code_rebplicate = self.container.get('service.merchant_voucher_complete_code_replication')
            ipos_order_created_replicate = self.container.get('service.ipos_order_created_replication')
            transaction_created_replicate = self.container.get('service.transaction_created_replication')
            registry \
                .add_listener(TransactionCreatedListener(transaction_created_replicate))\
                .add_listener(IposOrderCreatedListener(ipos_order_created_replicate))\
                .add_listener(MerchantVoucherCodeCreatedListener(merchant_voucher_complete_code_rebplicate)) \
                .run()

    def __set_log_level(self):
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s')

        logger = logging.getLogger()
        logger.setLevel(self.app_configuration.get('log.level'))

        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(formatter)
        stdout_handler.addFilter(lambda record: record.levelno <= logging.INFO)

        stderr_handler = logging.StreamHandler(sys.stderr)
        stderr_handler.setFormatter(formatter)
        stderr_handler.addFilter(lambda record: record.levelno > logging.INFO)

        logger.addHandler(stdout_handler)
        logger.addHandler(stderr_handler)

        sql_logger = logging.getLogger('sqlalchemy')
        sql_logger.propagate = False
