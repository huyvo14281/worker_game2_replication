import json
import logging
from datetime import datetime

import pytz
from sqlalchemy.orm import sessionmaker

from config.mongodb import MongoDb

LOGGER = logging.getLogger(__name__)


class MerchantVoucherCompletedCode:
    def __init__(self,
                 merchant_voucher_complete_code_session_maker: sessionmaker):
        self.session_maker = merchant_voucher_complete_code_session_maker

    def create_code(self, create_code: str):
        self.__save_code(create_code)

    def update_code(self, update_code: str):
        self.__save_code(update_code)

    # Save code to DATABASE
    def __save_code(self, save_code: str):
        data = json.loads(save_code)
        # data = save_code

        readl_time = datetime.now(pytz.timezone("Asia/Ho_Chi_Minh"))
        data["arrivalDate"] = readl_time

        self.__container = MongoDb()
        myclient = self.__container.get('mongo.client')
        myclient.insert(data)
