import mongoengine as me
import datetime

class CPUInformation(me.EmbeddedDocument):
    frequency = me.FloatField(default=0) # MHz unit
    count   = me.IntField(required=True, default=0)
    used    = me.FloatField(default=0) # show in percent
    used_per_cpu  = me.ListField(me.FloatField())
    
class MemoryInformation(me.EmbeddedDocument):
    total   = me.IntField(required=True, default=0)
    used    = me.IntField(default=0)
    free    = me.IntField(default=0)

class DiskInformation(me.EmbeddedDocument):
    total   = me.IntField(required=True, default=0)
    used    = me.IntField(default=0)
    free    = me.IntField(default=0)
    percent = me.FloatField(default=0) # show in percent

class VMInstance(me.EmbeddedDocument):
    name            = me.StringField(max_length=100, required=True)
    
    instance_id     = me.StringField(required=True)
    image_id        = me.StringField(required=True)
    
    # vm information
    kernel          = me.StringField()
    ramdisk         = me.StringField()   
    instance_type   = me.StringField(required=True)
    
    ip_address      = me.StringField()
    private_ip_address = me.StringField()
    
    started_instance_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    terminated_instance_date = me.DateTimeField()
    
    status          = me.StringField(required=True, default='pending')
    
    extra           = me.DictField()


class ComputeNode(me.Document):
    meta = {'collection': 'compute_nodes'}
    
    name    = me.StringField(max_length=100, required=True)
    system  = me.StringField(max_length=100)
    host    = me.StringField(max_length=100, required=True)
    machine = me.StringField(max_length=100)
    cpu     = me.EmbeddedDocumentField("CPUInformation", required=True, default=CPUInformation())
    memory  = me.EmbeddedDocumentField("MemoryInformation", required=True, default=MemoryInformation())
    disk    = me.EmbeddedDocumentField("DiskInformation", required=True, default=DiskInformation())
    
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    
    updated_resource_date = me.DateTimeField(required=True, default=datetime.datetime.now)

    vm      = me.EmbeddedDocumentField(VMInstance)
    
    extra           = me.DictField()
    
    def is_vm(self):
        if self.vm is None:
            return False
        
        return True
    
    def is_online(self):
        delta = datetime.timedelta(minutes=1)
        now = datetime.datetime.now()
                
        if self.updated_resource_date > now-delta:
            if self.cpu.used > 0 or self.memory.used > 0:
                return True
        
        return False
    
