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
    updated_date  = DateTimeField(required=True, default=datetime.datetime.now)
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
    
    created_date = DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = DateTimeField(required=True, default=datetime.datetime.now)
    
    project     = ReferenceField('Project', required=True, dbref=True)
    owner       = ReferenceField("User", required=True, dbref=True)
    

class ProcessorCommand(Document):
    meta = {'collection': 'processor_commands'}
    
    processor       = ReferenceField("Processor", dbref=True)
    attributes      = DictField()
    action          = StringField(required=True, default='no-operating')
    status          = StringField(required=True, default='waiting')
    compute_node    = EmbeddedDocumentField("ComputeNode")
    
    command_type    = StringField(required=True, default="system")
    commanded_date    = DateTimeField(required=True, default=datetime.datetime.now)
    processed_date    = DateTimeField(required=True, default=datetime.datetime.now)
    completed_date   = DateTimeField()
    
    updated_date     = DateTimeField(required=True, default=datetime.datetime.now)
    owner           = ReferenceField("User", dbref=True)
    message         = StringField(required=True, default='')
    
    extra           = DictField()
    
    command_type_option = ["system", "user"]

class ProcessorCommandQueue(Document):
    meta = {'collection': 'processor_command_queue'}
    
    processor_command    = ReferenceField("ProcessorCommand", dbref=True)
    
    
class ProcessorRunFail(Document):
    meta = {'collection': 'processor_run_fail'}
    
    processor       = ReferenceField("Processor", dbref=True)
    compute_node    = ReferenceField("ComputeNode", dbref=True)
    reported_date   = DateTimeField(required=True, default=datetime.datetime.now)
    processed_date  = DateTimeField(required=True, default=datetime.datetime.now)
    message         = StringField(required=True, default='')

