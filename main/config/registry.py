import logging
from typing import List

from kombu import Exchange, Queue, Connection
from kombu.mixins import ConsumerProducerMixin

from listener.listener import Listener

LOGGER = logging.getLogger(__name__)


class Registry(ConsumerProducerMixin):

    def __init__(self, connection: Connection, connect_max_retries: int):
        self.connection: Connection = connection
        self.connect_max_retries = connect_max_retries
        self.listeners: List[Listener] = []

    def add_listener(self, listener: Listener) -> 'Registry':
        if listener is None:
            raise Exception('Listener can\'t be none')
        binding = listener.get_binding()
        if binding is None:
            raise Exception('Binding can\'t be None')
        listener.set_producer(self.producer)
        self.listeners.append(listener)
        return self

    def get_consumers(self, Consumer, channel):
        return [Consumer(
            queues=[Queue(
                name=listener.get_binding().queue_name,
                exchange=Exchange(listener.get_binding().exchange, 'topic'),
                routing_key=listener.get_binding().routing_key,
                durable=True
            )],
            accept=['json'],
            callbacks=[Registry.__to_callback(listener)]
        ) for listener in self.listeners]

    @staticmethod
    def __to_callback(listener: Listener):
        def callback(payload, message):
            try:
                # listener.on_message(Utils.dict_to_tuple(payload), message)
                listener.on_message(payload, message)
            except Exception as ex:
                LOGGER.exception(ex)
            finally:
                message.ack()

        return callback
