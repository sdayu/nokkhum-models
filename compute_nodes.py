from mongoengine import *
import datetime

class CPUInformation(EmbeddedDocument):
    frequency = FloatField(default=0) # MHz unit
    count   = IntField(required=True, default=0)
    used    = FloatField(default=0) # show in percent
    used_per_cpu  = ListField(FloatField())
    
class MemoryInformation(EmbeddedDocument):
    total   = IntField(required=True, default=0)
    used    = IntField(default=0)
    free    = IntField(default=0)

class DiskInformation(EmbeddedDocument):
    total   = IntField(required=True, default=0)
    used    = IntField(default=0)
    free    = IntField(default=0)
    percent = FloatField(default=0) # show in percent

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
    
    started_instance_date = DateTimeField(required=True, default=datetime.datetime.now)
    terminated_instance_date = DateTimeField()
    
    status          = StringField(required=True, default='pending')
    
    extra           = DictField()


class ComputeNode(Document):
    meta = {'collection': 'compute_nodes'}
    
    name    = StringField(max_length=100, required=True)
    system  = StringField(max_length=100)
    host    = StringField(max_length=100, required=True)
    machine = StringField(max_length=100)
    cpu     = EmbeddedDocumentField("CPUInformation", required=True, default=CPUInformation())
    memory  = EmbeddedDocumentField("MemoryInformation", required=True, default=MemoryInformation())
    disk    = EmbeddedDocumentField("DiskInformation", required=True, default=DiskInformation())
    
    created_date = DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = DateTimeField(required=True, default=datetime.datetime.now)

    vm      = EmbeddedDocumentField(VMInstance)
    
    extra           = DictField()
    
    def is_vm(self):
        if self.vm is None:
            return False
        
        return True
    
    def is_online(self):
        delta = datetime.timedelta(minutes=1)
        now = datetime.datetime.now()
                
        if self.updated_date > now-delta:
            return True
        
        return False
    
