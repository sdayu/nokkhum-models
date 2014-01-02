'''
Created on Dec 28, 2013

@author: yoschanin.s
'''
import datetime
from mongoengine import *

class GroupCollboratorPermission(EmbeddedDocument):
    processor   = ReferenceField('Processor', required=True, dbref=True)
    permissions = ListField(StringField(default='view'))

class GroupCollaborator(EmbeddedDocument):
    user        = ReferenceField('User', required=True, dbref=True)
    camera_permissions = ListField(EmbeddedDocumentField(GroupCollboratorPermission))
    
    permissions = ListField(StringField(default='user'))
    create_date = DateTimeField(required=True, default=datetime.datetime.now)

class Group(Document):
    meta = {'collection': 'groups'}

    name        = StringField(required=True)
    description = StringField(required=True)
    status      = StringField(required=True, default='active')
    
    create_date = DateTimeField(required=True, default=datetime.datetime.now)
    update_date = DateTimeField(required=True, default=datetime.datetime.now)
    
    ip_address  = StringField(max_length=100, required=True, default='0.0.0.0')
    collaborators = ListField(EmbeddedDocumentField(GroupCollaborator))
    