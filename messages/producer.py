'''
Created on Dec 23, 2011

@author: boatkrap
'''
from __future__ import with_statement


from kombu.common import maybe_declare
from kombu.pools import producers

from . import connection

class Producer:
    def __init__(self, connection):
        self._connection = connection
        
        self._producer = self._connection.Producer(exchange=self._connection.exchange,
            serializer="json", routing_key=self._connection.routing_key)
            
    def send(self, message):
        self._producer.publish(message)
        
class ProducerFactory:
    def __init__(self):
        self.connection = None
        self.producer = None
        
    def get_producer(self, name):
        if name == "nokkhum_compute.update_status":
            if self.connection is None:
                self.connection = connection.Connection()
            self.producer = Producer(self.connection)
            return self.producer