from kombu import BrokerConnection

class Connection:
    def __init__(self):
        self.connection = BrokerConnection("amqp://guest:guest@localhost:5672/nokkhum")
    
    def get_broker_connection(self):
        return self.connection

        
default_connection = Connection()