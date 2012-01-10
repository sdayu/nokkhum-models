from kombu import BrokerConnection

class Connection:
    def __init__(self):
        self.connection = BrokerConnection("amqp://guest:guest@localhost:5672/nokkhum")
        self.channel = self.get_new_channel()
        
    def get_broker_connection(self):
        return self.connection
    
    def get_channel(self):
        return self.channel
    
    def get_new_channel(self):
        return self.connection.channel()

        
default_connection = Connection()