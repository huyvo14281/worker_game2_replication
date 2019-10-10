from kombu import Message


class Binding:

    def __init__(self, exchange: str = None, queue_name: str = None, routing_key: str = None) -> None:
        if exchange is None:
            raise Exception('Exchange can\'t be none')

        if queue_name is None:
            raise Exception('Queue name can\'t be none')

        if routing_key is None:
            raise Exception('Routing key can\'t be none')

        self.routing_key = routing_key
        self.queue_name = queue_name
        self.exchange = exchange


class Listener:

    def __init__(self):
        self.producer = None

    def set_producer(self, producer):
        self.producer = producer

    def get_binding(self) -> Binding:
        raise NotImplementedError

    def on_message(self, payload, message: Message):
        raise NotImplementedError
