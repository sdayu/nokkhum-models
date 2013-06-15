'''
Created on Aug 7, 2012

@author: boatkrap
'''
from mongoengine import *
import datetime

class CameraProcessStatus(Document):
    meta = {'collection': 'camera_process_status'}
    
    report_date     = DateTimeField(required=True, default=datetime.datetime.now)
    cpu             = FloatField(default=0)
    memory          = IntField(default=0)
    threads         = IntField(default=0)
    messages        = ListField()
    
    camera          = ReferenceField("Camera", dbref=True, required=True)
    compute_node_report = ReferenceField("ComputeNodeReport", dbref=True, required=True)

class ComputeNodeReport(Document):
    meta = {'collection': 'compute_node_report'}
    
    compute_node    = ReferenceField("ComputeNode", dbref=True)
    
    report_date     = DateTimeField(required=True, default=datetime.datetime.now)
    
    cpu             = EmbeddedDocumentField("CPUInformation", required=True)
    memory          = EmbeddedDocumentField("MemoryInformation", required=True)
    disk            = EmbeddedDocumentField("DiskInformation", required=True)
    
    camera_process_status = ListField(ReferenceField(CameraProcessStatus, dbref=True))
    
