'''
Created on Dec 23, 2011

@author: boatkrap
'''
import kombu
import kombu.messaging
from kombu import Exchange


from . import connection
from . import queues

class Consumer:

    def __init__(self, exchange_name, channel, routing_key, callback=[]):
        self.exchange_name = exchange_name
        self.callback = callback
        self.routing_key = routing_key
        self._consumer = None
        self.reconnect(channel)

    def reconnect(self, channel):
        exchange = Exchange(self.exchange_name, type="direct", durable=True)
        queue = queues.QueueFactory().get_queue(exchange, self.routing_key)
        queue(channel).declare()
        self._consumer = kombu.messaging.Consumer(channel, queue, callbacks=self.callback, no_ack=True)
    
    def register(self, callback):
        self._consumer.register_callback(callback)
        self.callback.append(callback)
        self.consume()
    
    def consume(self):
        self._consumer.consume()

class ConsumerFactory:
    def __init__(self):
        self.connection = None
        self.consumer = None
        
    def get_consumer(self, name):
        if name == "nokkhum_compute.update_status":
            routing_key = "nokkhum_compute.update_status"
            if self.connection is None:
                self.connection = connection.default_connection.get_broker_connection()
            
            channel = self.connection.channel()
            
            self.consumer = Consumer("nokkunm_compute", channel, routing_key)
            return self.consumer
    
    def get_connection(self):
        if self.connection is None:
            self.connection = connection.default_connection.get_broker_connection()
            
        return self.connection