from mongoengine import *
import datetime
from .users import User

class Manufactory(Document):
    meta = {'collection': 'camera_manufactories'}
    
    name        = StringField(max_length=100, required=True)
    create_date = DateTimeField(required=True, default=datetime.datetime.now)
    
class CameraModel(Document):
    meta = {'collection': 'camera_models'}
    
    name        = StringField(max_length=100, required=True)
    manufactory = ReferenceField(Manufactory, required=True, dbref=True)
    create_date = DateTimeField(required=True, default=datetime.datetime.now)    
    
class Camera(Document):
    meta = {'collection': 'cameras'}
    
    username    = StringField(max_length=100, required=True)
    password    = StringField()
    name        = StringField(required=True)
    host        = StringField()
    port        = IntField()
    video_url   = StringField(required=True)
    audio_url   = StringField()
    image_url   = StringField()
    image_size  = StringField(required=True)
    fps         = IntField(required=True)
    status      = StringField(required=True, default='active')
    
    owner       = ReferenceField(User, required=True, dbref=True)
    
    camera_model = ReferenceField('CameraModel', required=True, dbref=True)
    project     = ReferenceField('Project', required=True, dbref=True)
    
    create_date = DateTimeField(required=True, default=datetime.datetime.now)
    update_date = DateTimeField(required=True, default=datetime.datetime.now)
    
    ip_address  = StringField(max_length=100, required=True, default='0.0.0.0')
