import logging

from listener.listener import Listener, Binding
from service.ipos_order_created import IposOrderCreated

LOGGER = logging.getLogger(__name__)

class IposOrderCreatedListener(Listener):

    def __init__(self, ipos_order_created: IposOrderCreated):
        super().__init__()
        self.ipos_order_created = ipos_order_created

    def get_binding(self):
        return Binding(
            queue_name='ipos_order.created.worker_game_replication',
            routing_key='pos_gateway.ipos_order_created',
            exchange='event')

    def on_message(self, payload, message):
        self.ipos_order_created.create_code(payload)

