'''
Created on Dec 23, 2011

@author: boatkrap
'''
from kombu import Queue

class QueueFactory:
    def get_queue(self, exchange, routing_key):
        import fnmatch, re
        regex = fnmatch.translate('nokkhum_compute.*.rpc_request')
        reobj_rpc_request = re.compile(regex)
        regex = fnmatch.translate('nokkhum_compute.*.rpc_response')
        reobj_rpc_response = re.compile(regex)

        if routing_key == "nokkhum_compute.update_status":
            return Queue("nokkhum_compute.update_status", exchange, routing_key=routing_key)
        elif reobj_rpc_request.match(routing_key):
            return Queue("nokkunm_compute.rpc_request", exchange, routing_key=routing_key)
        elif reobj_rpc_response.match(routing_key):
            return Queue("nokkunm_compute.rpc_response", exchange, routing_key=routing_key)
        else:
            return None
