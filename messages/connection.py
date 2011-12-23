from kombu import BrokerConnection
from kombu import Exchange, Queue

class Connection:
    def __init__(self):
        self.connection = BrokerConnection("amqp://guest:guest@localhost:5672/nokkhum")
        self.routing_key = "nokkhum_compute.update_status"
        self.exchange = Exchange("nokkhum_compute", type="direct", durable=True)
        self.queue = Queue("update_status", self.exchange, routing_key=self.routing_key)
    
        with self.connection.channel() as channel:
            self.queue(channel).declare()