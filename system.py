'''
Created on Nov 8, 2011

@author: boatkrap
'''

from mongoengine import *
import datetime

class CameraCommandQueue(Document):
    meta = {'collection': 'camera_command_queue'}
    
    id      = SequenceField(required=True, unique=True, primary_key=True)
    camera  = ReferenceField("Camera")
    action  = StringField(required=True, default='No-operating')
    status  = StringField(required=True, default='Waiting')
    command_date    = DateTimeField(required=True, default=datetime.datetime.now())
    update_date     = DateTimeField(required=True, default=datetime.datetime.now())
    owner   = ReferenceField("User")
    
class CommandLog(Document):
    meta = {'collection': 'command_log'}
    
    id      = SequenceField(required=True, unique=True, primary_key=True)
    camera  = ReferenceField("Camera")
    action  = StringField(required=True, default='Waiting')
    owner   = ReferenceField("User")
    attributes      = DictField()
    compute_node    = EmbeddedDocumentField("ComputeNode")
    command_date    = DateTimeField(required=True, default=datetime.datetime.now())
    complete_date   = DateTimeField(required=True, default=datetime.datetime.now())