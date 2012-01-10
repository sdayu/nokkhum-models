'''
Created on Dec 23, 2011

@author: boatkrap
'''
import kombu
import kombu.messaging
from kombu import Exchange


from . import connection
from . import queues

import logging
logger = logging.getLogger(__name__)

class Consumer:

    def __init__(self, exchange_name, channel, routing_key, callback=None):
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
        self.consume()
    
    def register(self, callback):
        self._consumer.register_callback(callback)
        self.callback = callback
    
    def consume(self):
        self._consumer.consume()
        
class TopicConsumer(Consumer):
    
    def __init__(self, exchange_name, channel, routing_key, callback=None):
        Consumer.__init__(self, exchange_name, channel, routing_key)
        
    def reconnect(self, channel):
        exchange = Exchange(self.exchange_name, type="topic", durable=True)
        queue = queues.QueueFactory().get_queue(exchange, self.routing_key)
        queue(channel).declare()
        self._consumer = kombu.messaging.Consumer(channel, queue, callbacks=self.callback, no_ack=True)
        self.consume()

class ConsumerFactory:
    def __init__(self):
        self.connection = None
        
    def get_consumer(self, key):
        if self.connection is None:
            self.connection = connection.default_connection.get_broker_connection()
            
        if key == "nokkhum_compute.update_status":
            routing_key = "nokkhum_compute.update_status"
            
            channel = connection.default_connection.get_channel()
            
            consumer = Consumer("nokkunm_compute", channel, routing_key)
            return consumer
        else:
            import fnmatch, re
            regex = fnmatch.translate('nokkhum_compute.*.*')
            reobj = re.compile(regex)
            if reobj.match(key):
                routing_key = key
                channel = connection.default_connection.get_channel()
                consumer = TopicConsumer("nokkunm_compute.command", channel, routing_key)
#                logger.debug("get topic cons: %s"%consumer)
                return consumer
    
    def get_connection(self):
        if self.connection is None:
            self.connection = connection.default_connection.get_broker_connection()
            
        return self.connection