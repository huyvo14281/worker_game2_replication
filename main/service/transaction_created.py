import logging

from sqlalchemy.orm import sessionmaker

LOGGER = logging.getLogger(__name__)


class TransactionCreated:
    def __init__(self,
                 transaction_created_session_maker: sessionmaker):
        self.session_maker = transaction_created_session_maker

    def create_code(self, create_code: str):
        self.__save_code(create_code)

    def update_code(self, update_code: str):
        self.__save_code(update_code)

    # Save code to DATABASE
    def __save_code(self, save_code: str):
        LOGGER.info('transaction created!!!')
