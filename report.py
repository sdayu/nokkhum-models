'''
Created on Aug 7, 2012

@author: boatkrap
'''
import mongoengine as me
import datetime

class ProcessorStatus(me.Document):
    meta = {'collection': 'processor_status'}
    
    reported_date     = me.DateTimeField(required=True, default=datetime.datetime.now)
    cpu             = me.FloatField(default=0)
    memory          = me.IntField(default=0)
    threads         = me.IntField(default=0)
    messages        = me.ListField()
    
    processor          = me.ReferenceField('Processor', dbref=True, required=True)
    compute_node_report = me.ReferenceField('ComputeNodeReport', dbref=True, required=True)

class ComputeNodeReport(me.Document):
    meta = {'collection': 'compute_node_report'}
    
    compute_node    = me.ReferenceField('ComputeNode', dbref=True)
    
    reported_date     = me.DateTimeField(required=True, default=datetime.datetime.now)
    
    cpu             = me.EmbeddedDocumentField('CPUInformation', required=True)
    memory          = me.EmbeddedDocumentField('MemoryInformation', required=True)
    disk            = me.EmbeddedDocumentField('DiskInformation', required=True)
    
    processor_status = me.ListField(me.ReferenceField(ProcessorStatus, dbref=True))
    
