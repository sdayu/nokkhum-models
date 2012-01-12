'''
Created on Dec 23, 2011

@author: boatkrap
'''
from __future__ import with_statement


from kombu.common import maybe_declare
from kombu.pools import producers
from kombu import Exchange
import kombu

from . import queues

import logging
logger = logging.getLogger(__name__)

class Publisher:
    def __init__(self, exchange_name, channel, routing_key):

        self.exchange_name = exchange_name
        self.routing_key = routing_key
        self._producer = None
        
        self.reconnect(channel)
        
        
    def reconnect(self, channel):
        exchange = Exchange(self.exchange_name, type="direct", durable=True)
        queue = queues.QueueFactory().get_queue(exchange, self.routing_key)
        queue(channel).declare()
        self._producer = kombu.messaging.Producer(exchange=exchange,
            channel=channel, serializer="json", 
            routing_key=self.routing_key)
            
    def send(self, message, routing_key=None):
        self._producer.publish(message, routing_key=routing_key)
        
class TopicPublisher(Publisher):
    def __init__(self, exchange_name, channel, routing_key):
        Publisher.__init__(self, exchange_name, channel, routing_key) 
    
    def reconnect(self, channel):
        exchange = Exchange(self.exchange_name, type="topic", durable=True)
        queue = queues.QueueFactory().get_queue(exchange, self.routing_key)
        queue(channel).declare()
#        logger.debug( "reconnect topic")
        
        self._producer = kombu.messaging.Producer(exchange=exchange,
            channel=channel, serializer="json", 
            routing_key=self.routing_key)
        
        
class PublisherFactory:
    def __init__(self):
        self.connection = None
    
    
    def get_publisher(self, key):
        from . import connection
        publisher = None
        logger.debug("routing_key: %s"% key)
        if key == "nokkhum_compute.update_status":
            routing_key = "nokkhum_compute.update_status"
            channel = connection.default_connection.get_channel()
            publisher = Publisher("nokkunm_compute.update_status", channel, routing_key)
            # logger.debug("get pub: %s"% publisher)
            return publisher
        
        else:
            import fnmatch, re
            regex = fnmatch.translate('nokkhum_compute.*.rpc_*')
            reobj = re.compile(regex)
            if reobj.match(key):
                routing_key = key
                channel = connection.default_connection.get_channel()
                if "nokkhum_compute.*" in routing_key:
                    publisher = TopicPublisher("nokkunm_compute.rpc", channel, routing_key)
                else:
                    publisher = TopicPublisher("nokkunm_compute.compute_rpc", channel, routing_key)
                # logger.debug("get pub: %s"%publisher)
                return publisher
            
        return publisher
            