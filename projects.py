'''
Created on Jun 21, 2012

@author: boatkrap
'''
import datetime
from mongoengine import *

from .cameras import Camera

class Project(Document):
    meta = {'collection': 'projects'}
    id          = SequenceField(required=True, unique=True, primary_key=True)
    name        = StringField(required=True)
    description = StringField(required=True)
    status      = StringField(required=True, default='Active')
    
    create_date = DateTimeField(required=True, default=datetime.datetime.now)
    update_date = DateTimeField(required=True, default=datetime.datetime.now)
    
    ip_address  = StringField(max_length=100, required=True, default='0.0.0.0')
    
    owner       = ReferenceField("User", required=True)
    
    
    def get_camera_number(self):
        return Camera.objects(project = self).count()