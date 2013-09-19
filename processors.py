'''
Created on Nov 8, 2011

@author: boatkrap
'''

from mongoengine import *
import datetime
import bson

class ProcessorOperating(EmbeddedDocument):
    user_command = StringField(required=True, default="suspend")
    status       = StringField(required=True, default="stop")
    update_date  = DateTimeField(required=True, default=datetime.datetime.now)
    user_command_log = ListField(ObjectIdField())
    
    compute_node = ReferenceField("ComputeNode", dbref=True)
    
    
    define_operating_status = ["start", "starting", "running", "stopping", "stop"]
    define_user_commands    = ["stop", "run", "suspend"]

class Processor(Document):
    meta = {'collection': 'processors'}
    
    name = StringField()
    cameras = ListField(ReferenceField('Camera', dbref=True))
    
    storage_period = IntField(required=True, default="0") # in day
    
    image_processors  = ListField(DictField())
    operating   = EmbeddedDocumentField("ProcessorOperating", required=True, default=ProcessorOperating)
    status      = StringField(required=True, default='active')
    
    create_date = DateTimeField(required=True, default=datetime.datetime.now)
    update_date = DateTimeField(required=True, default=datetime.datetime.now)
    
    project     = ReferenceField('Project', required=True, dbref=True)
    owner       = ReferenceField("User", required=True, dbref=True)
    

class ProcessorCommand(EmbeddedDocument):
    id  = ObjectIdField(primary=True, required=True, default=bson.objectid.ObjectId())
    processor  = ReferenceField("Processor", dbref=True)
    attributes      = DictField()
    action  = StringField(required=True, default='no-operating')
    status  = StringField(required=True, default='waiting')
    compute_node    = EmbeddedDocumentField("ComputeNode")
    
    command_type    = StringField(required=True, default="system")
    command_date    = DateTimeField(required=True, default=datetime.datetime.now)
    process_date    = DateTimeField(required=True, default=datetime.datetime.now)
    complete_date   = DateTimeField()
    
    update_date     = DateTimeField(required=True, default=datetime.datetime.now)
    owner   = ReferenceField("User", dbref=True)
    message = StringField()
    
    extra   = DictField()
    
    command_type_option = ["system", "user"]

class ProcessorCommandQueue(Document):
    meta = {'collection': 'processor_command_queue'}
    
    processor_command    = EmbeddedDocumentField("ProcessorCommand")
    
class CommandLog(Document):
    meta = {'collection': 'command_log'}
    
    processor_command    = EmbeddedDocumentField("ProcessorCommand")
    
    
class ProcessorRunningFail(Document):
    meta = {'collection': 'processor_running_fail'}
    
    processor       = ReferenceField("Processor", dbref=True)
    compute_node    = ReferenceField("ComputeNode", dbref=True)
    report_time     = DateTimeField(required=True, default=datetime.datetime.now)
    process_time    = DateTimeField(required=True, default=datetime.datetime.now)
    message         = StringField()

