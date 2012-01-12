'''
Created on Dec 23, 2011

@author: boatkrap
'''
import kombu
import kombu.messaging
from kombu import Exchange

from . import queues

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
        
    def get_consumer(self, key):
        from . import connection
            
        consumer = None
        if key == "nokkhum_compute.update_status":
            routing_key = "nokkhum_compute.update_status"
            
            channel = connection.default_connection.get_channel()
            
            consumer = Consumer("nokkunm_compute", channel, routing_key)
            return consumer
        else:
            import fnmatch, re
            regex = fnmatch.translate('nokkhum_compute.*.rpc_*')
            reobj = re.compile(regex)
            if reobj.match(key):
                routing_key = key
                channel = connection.default_connection.get_channel()
                
                if "nokkhum_compute.*" in routing_key:
                    consumer = TopicConsumer("nokkunm_compute.rpc", channel, routing_key)
                else:
                    consumer = TopicConsumer("nokkunm_compute.compute_rpc", channel, routing_key)
#                logger.debug("get pub: %s"%publisher)
                return consumer