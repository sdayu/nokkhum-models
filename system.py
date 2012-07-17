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
    message = StringField()
    
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
    status          = StringField(required=True)
    message         = StringField()
    
class CameraRunningFail(Document):
    meta = {'collection': 'camera_running_fail'}
    
    camera          = ReferenceField("Camera")
    compute_node    = ReferenceField("ComputeNode")
    report_time     = DateTimeField(required=True, default=datetime.datetime.now())
    process_time    = DateTimeField(required=True, default=datetime.datetime.now())
    message         = StringField()

