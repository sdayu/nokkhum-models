'''
Created on Dec 23, 2011

@author: boatkrap
'''
from kombu import Queue

class QueueFactory:
    def get_queue(self, exchange, routing_key):
        import fnmatch, re
        regex = fnmatch.translate('nokkhum_compute.*.*')
        reobj = re.compile(regex)

        if routing_key == "nokkhum_compute.update_status":
            return Queue("nokkhum_compute.update_status", exchange, routing_key=routing_key)
        elif reobj.match(routing_key):
            return Queue("nokkunm_compute.command", exchange, routing_key=routing_key)
        else:
            return None
