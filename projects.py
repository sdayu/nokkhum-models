'''
Created on Jun 21, 2012

@author: boatkrap
'''
import datetime
from mongoengine import *

class CollboratorPermission(EmbeddedDocument):
    processor      = ReferenceField('Processor', required=True, dbref=True)
    permissions = ListField(StringField(default='view'))

class Collaborator(EmbeddedDocument):
    user        = ReferenceField('User', required=True, dbref=True)
    camera_permissions = ListField(EmbeddedDocumentField(CollboratorPermission))
    
    permissions = ListField(StringField(default='view'))
    create_date = DateTimeField(required=True, default=datetime.datetime.now)

class Project(Document):
    meta = {'collection': 'projects'}

    name        = StringField(required=True)
    description = StringField(required=True)
    status      = StringField(required=True, default='active')
    
    create_date = DateTimeField(required=True, default=datetime.datetime.now)
    update_date = DateTimeField(required=True, default=datetime.datetime.now)
    
    ip_address  = StringField(max_length=100, required=True, default='0.0.0.0')
    
    owner       = ReferenceField('User', required=True, dbref=True)
    collaborators = ListField(EmbeddedDocumentField(Collaborator))
    gcollaborators = ListField(ReferenceField('Group', dbref=True))
    
    def get_camera_number(self):
        from .cameras import Camera
        return Camera.objects(project = self).count()
    
    def get_processor_number(self):
        from .processors import Processor
        return Processor.objects(project = self).count()