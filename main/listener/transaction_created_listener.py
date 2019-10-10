import logging

from listener.listener import Listener, Binding
from service.transaction_created import TransactionCreated

LOGGER = logging.getLogger(__name__)

class TransactionCreatedListener(Listener):

    def __init__(self, transaction_created: TransactionCreated):
        super().__init__()
        self.transaction_created = transaction_created

    def get_binding(self):
        return Binding(
            queue_name='transaction.created.worker_game_replication',
            routing_key='merchant.loyalty.transaction_created',
            exchange='event')

    def on_message(self, payload, message):
        self.transaction_created.create_code(payload)

