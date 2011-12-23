'''
Created on Dec 23, 2011

@author: boatkrap
'''
from kombu import Queue

class QueueFactory:
    def get_queue(self, exchange, routing_key):
        if routing_key == "nokkhum_compute.update_status":
            return Queue("update_status", exchange, routing_key=routing_key)
