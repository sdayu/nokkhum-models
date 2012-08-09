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
    
    camera  = ReferenceField("Camera")

class ComputeNodeReport(Document):
    meta = {'collection': 'compute_node_report'}
    
    compute_node    = ReferenceField("ComputeNode")
    
    report_date     = DateTimeField(required=True, default=datetime.datetime.now)
    
    cpu             = EmbeddedDocumentField("CPUInfomation", required=True)
    memory          = EmbeddedDocumentField("MemoryInfomation", required=True)
      
    camera_process_status = ListField(EmbeddedDocumentField(CameraProcessStatus))
    
