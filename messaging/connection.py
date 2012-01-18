from kombu import BrokerConnection

#import logging
#logger = logging.getLogger(__name__)

class Connection:
    def __init__(self, url):
        self.url = url
        self.connection = self.reconnect(self.url)
        self._running = True
        self.channel = self.get_new_channel()
        from . import rpc
        self.rpc_factory = rpc.RpcFactory()
    
    def get_broker_connection(self):
        if self.connection is None:
            self.reconnect(self.url)
            
        return self.connection
    
    def get_channel(self):
        if self.channel is None:
            self.channel = self.get_new_channel()
        return self.channel
    
    def get_new_channel(self):
        if self.connection is None:
            self.reconnect(self.url)
        return self.connection.channel()
    
    def get_rpc_factory(self):
        return self.rpc_factory
    
    def reconnect(self, url):
        self.connection = BrokerConnection(url)
        
    def drain_events(self):
        while self._running:
            self.connection.drain_events()
            
    
    def release(self):
        self._running = False
        self.connection.release()
        self.connection = None
        
default_connection = None

def initial(url):
    global default_connection
    default_connection = Connection(url)
    