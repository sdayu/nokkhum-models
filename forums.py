'''
Created on Jan 16, 2014

@author: yoschanin.s
'''
import datetime
from mongoengine import *

class Reply(EmbeddedDocument):
    user        = ReferenceField('User', required=True, dbref=True)
    description = StringField(required=True)
    create_date = DateTimeField(required=True, default=datetime.datetime.now)

class Forum(Document):
    meta = {'collection': 'forums'}
    
    owner       = ReferenceField('User', required=True, dbref=True)
    group       = ReferenceField('Group', required=True, dbref=True)
    
    description = StringField(required=True)
    
    create_date = DateTimeField(required=True, default=datetime.datetime.now)
    update_date = DateTimeField(required=True, default=datetime.datetime.now)

    replys = ListField(EmbeddedDocumentField(Reply))
    