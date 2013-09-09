'''
Created on Nov 8, 2011

@author: boatkrap
'''

from mongoengine import *
import datetime

class ProcessorOperating(EmbeddedDocument):
    user_command = StringField(required=True, default="suspend")
    status       = StringField(required=True, default="stop")
    update_date  = DateTimeField(required=True, default=datetime.datetime.now)
    compute_node = ReferenceField("ComputeNode", dbref=True)
    
    define_operating_status = ["start", "starting", "running", "stopping", "stop"]
    define_user_commands    = ["stop", "run", "suspend"]

class Processor(Document):
    meta = {'collection': 'processors'}
    
    cameras = ListField(ReferenceField('Camera', dbref=True))
    
    storage_periods = IntField(required=True, default="0") # in day
    
    processors  = ListField(DictField())
    operating   = EmbeddedDocumentField("ProcessorOperating", required=True)
    
    create_date = DateTimeField(required=True, default=datetime.datetime.now)
    update_date = DateTimeField(required=True, default=datetime.datetime.now)
    

class ProcessorCommand(EmbeddedDocument):
    processor  = ReferenceField("Processor", dbref=True)
    attributes      = DictField()
    action  = StringField(required=True, default='no-operating')
    status  = StringField(required=True, default='waiting')
    compute_node    = EmbeddedDocumentField("ComputeNode")
    
    command_date    = DateTimeField(required=True, default=datetime.datetime.now)
    process_date    = DateTimeField(required=True, default=datetime.datetime.now)
    complete_date   = DateTimeField()
    
    update_date     = DateTimeField(required=True, default=datetime.datetime.now)
    owner   = ReferenceField("User", dbref=True)
    message = StringField()
    
    extra   = DictField()

class ProcessorCommandQueue(Document):
    meta = {'collection': 'processor_command_queue'}
    
    id                  = SequenceField(required=True, unique=True, primary_key=True)
    procesor_command    = EmbeddedDocumentField("ProcessorCommand")
    
class CommandLog(Document):
    meta = {'collection': 'command_log'}
    
    command_id          = SequenceField(required=True, unique=True, primary_key=True)
    procesor_command    = EmbeddedDocumentField("ProcessorCommand")
    
    
class ProcessorRunningFail(Document):
    meta = {'collection': 'processor_running_fail'}
    
    camera          = ReferenceField("Camera", dbref=True)
    compute_node    = ReferenceField("ComputeNode", dbref=True)
    report_time     = DateTimeField(required=True, default=datetime.datetime.now)
    process_time    = DateTimeField(required=True, default=datetime.datetime.now)
    message         = StringField()

