'''
Created on Jun 21, 2012

@author: boatkrap
'''
import datetime
import mongoengine as me

class CollboratorPermission(me.EmbeddedDocument):
    processor      = me.ReferenceField('Processor', required=True, dbref=True)
    permissions = me.ListField(me.StringField(default='view'))

class Collaborator(me.EmbeddedDocument):
    user        = me.ReferenceField('User', required=True, dbref=True)
    camera_permissions = me.ListField(me.EmbeddedDocumentField(CollboratorPermission))
    
    permissions = me.ListField(me.StringField(default='view'))
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)

class Project(me.Document):
    meta = {'collection': 'projects'}

    name        = me.StringField(required=True)
    description = me.StringField(required=True)
    status      = me.StringField(required=True, default='active')
    
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    
    ip_address  = me.StringField(max_length=100, required=True, default='0.0.0.0')
    
    owner       = me.ReferenceField('User', required=True, dbref=True)
    collaborators = me.ListField(me.EmbeddedDocumentField(Collaborator))
    gcollaborators = me.ListField(me.ReferenceField('Group', dbref=True))
    
    def get_camera_number(self):
        from .cameras import Camera
        return Camera.objects(project = self).count()
    
    def get_processor_number(self):
        from .processors import Processor
        return Processor.objects(project = self).count()