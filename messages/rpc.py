'''
Created on Jan 11, 2012

@author: boatkrap
'''

import kombu.utils

from . import publisher
from . import consumer

import logging
logger = logging.getLogger(__name__)

import time

class RpcClient():
    def __init__(self):
        self._publisher = publisher.PublisherFactory().get_publisher("nokkhum_compute.*.rpc_request")
        self._consumer = consumer.ConsumerFactory().get_consumer("nokkhum_compute.*.rpc_request")
        
        self.message_pool = {}
        
        self.__regist_consumer_callback()
    
    def __regist_consumer_callback(self):
        def process_message(body, message):
            message.ack()
            if 'message_id' in body:
                self.message_pool[body['message_id']] = body
            else:
                logger.debug('message ignore by RPC: %s'%body)
                
    def call(self, message, routing_key):
        message_id = kombu.utils.uuid()
        message['message_id'] = message_id
        
        self.send(message, routing_key)
        
        while message_id not in self.message_pool.keys():
            time.sleep(0.01)
            
        response = self.message_pool[message_id]
        return response
        
    def send(self, message, routing_key):
        self._publisher.send(message, routing_key)