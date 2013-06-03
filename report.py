'''
Created on Aug 7, 2012

@author: boatkrap
'''
from mongoengine import *
import datetime

class CameraProcessStatus(EmbeddedDocument):
    cpu     = FloatField(default=0)
    memory  = IntField(default=0)
    threads = IntField(default=0)
    messages = ListField()
    
    camera  = ReferenceField("Camera", dbref=True)

class ComputeNodeReport(Document):
    meta = {'collection': 'compute_node_report'}
    
    compute_node    = ReferenceField("ComputeNode", dbref=True)
    
    report_date     = DateTimeField(required=True, default=datetime.datetime.now)
    
    cpu             = EmbeddedDocumentField("CPUInformation", required=True)
    memory          = EmbeddedDocumentField("MemoryInformation", required=True)
    disk    = EmbeddedDocumentField("DiskInformation", required=True, default=DiskInfomation())
    
    camera_process_status = ListField(EmbeddedDocumentField(CameraProcessStatus))
    
