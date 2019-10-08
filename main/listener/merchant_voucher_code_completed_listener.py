import logging

from listener.listener import Listener, Binding
from service.merchant_voucher_completed_code import MerchantVoucherCompletedCode

LOGGER = logging.getLogger(__name__)


class MerchantVoucherCodeCreatedListener(Listener):

    def __init__(self, merchant_voucher_completed_code: MerchantVoucherCompletedCode):
        super().__init__()
        self.merchant_voucher_completed_code = merchant_voucher_completed_code

    def get_binding(self):
        return Binding(
            queue_name='merchant_voucher_completed_code',
            routing_key='merchant.voucher.voucher_code_completed',
            exchange='event')

    def on_message(self, payload, message):
        self.merchant_voucher_completed_code.create_code(payload)
