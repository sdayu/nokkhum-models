'''
Created on Dec 23, 2011

@author: boatkrap
'''
from __future__ import with_statement


from kombu.common import maybe_declare
from kombu.pools import producers
from kombu import Exchange
import kombu

from . import connection
from . import queues

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
            
    def send(self, message):
        self._producer.publish(message)
        
class TopicPublisher(Publisher):
    
    def reconnect(self, channel):
        exchange = Exchange(self.exchange_name, type="topic", durable=True)
        queue = queues.QueueFactory().get_queue(exchange, self.routing_key)
        queue(channel).declare()
        
        self._producer = kombu.messaging.Producer(exchange=exchange,
            channel=channel, serializer="json", 
            routing_key=self.routing_key)  
        
class PublisherFactory:
    def __init__(self):
        self.connection = None
        self.publisher_pool = {}
    
    
    def get_producer(self, name):
        
        if self.connection is None:
            self.connection = connection.default_connection.get_broker_connection()
                
        if name == "nokkhum_compute.update_status":
            routing_key = "nokkhum_compute.update_status"
            if routing_key in self.publisher_pool.keys():
                return self.publisher_pool["nokkhum_compute.update_status"]
            
            channel = self.connection.channel()
            
            publisher = Publisher("nokkunm_compute", channel, routing_key)
            self.publisher_pool["nokkhum_compute.update_status"] = publisher
            return publisher
        
        elif name == "nokkhum_compute.update_status":