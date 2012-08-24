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

class VMInstance(EmbeddedDocument):
    name            = StringField(max_length=100, required=True)
    
    instance_id     = StringField(required=True)
    image_id        = StringField(required=True)
    
    # vm information
    kernel          = StringField()
    ramdisk         = StringField()   
    instance_type   = StringField(required=True)
    
    ip_address      = StringField()
    private_ip_address = StringField()
    
    start_instance_date     = DateTimeField(required=True, default=datetime.datetime.now)
    terminate_instance_date = DateTimeField()


class ComputeNode(Document):
    meta = {'collection': 'compute_nodes'}
    
    name    = StringField(max_length=100, required=True)
    system  = StringField(max_length=100)
    host    = StringField(max_length=100, required=True)
    machine = StringField(max_length=100)
    cpu     = EmbeddedDocumentField("CPUInfomation", required=True, default=CPUInfomation())
    memory  = EmbeddedDocumentField("MemoryInfomation", required=True, default=MemoryInfomation())
    
    create_date = DateTimeField(required=True, default=datetime.datetime.now)
    update_date = DateTimeField(required=True, default=datetime.datetime.now)

    vm      = EmbeddedDocumentField(VMInstance)
    
    def is_vm(self):
        if self.vm is None:
            return False
        
        return True
        

