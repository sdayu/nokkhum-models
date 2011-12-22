from mongoengine import *
import datetime

class CPUInfomation(EmbeddedDocument):
    count   = IntField(required=True, default=0)
    usage   = FloatField(default=0) # show in percent
    usage_per_cpu  = ListField(FloatField())
    
class MemoryInfomation(EmbeddedDocument):
    total   = IntField(required=True, default=0)
    used    = IntField(default=0)
    free    = IntField(default=0)
    
class ComputeNode(Document):
    meta = {'collection': 'compute_nodes'}
    
    name    = StringField(max_length=100, required=True)
    system  = StringField(max_length=100, required=True)
    host    = StringField(max_length=100, required=True)
    machine = StringField(max_length=100, required=True)
    port    = IntField(required=True)
    cpu     = EmbeddedDocumentField("CPUInfomation", required=True)
    memory  = EmbeddedDocumentField("MemoryInfomation", required=True)
    
    create_date = DateTimeField(required=True, default=datetime.datetime.now())
    update_date = DateTimeField(required=True, default=datetime.datetime.now())


