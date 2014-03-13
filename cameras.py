import mongoengine as me
import datetime
from .users import User

class Manufactory(me.Document):
    meta = {'collection': 'camera_manufactories'}
    
    name        = me.StringField(max_length=100, required=True)
    create_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    
class CameraModel(me.Document):
    meta = {'collection': 'camera_models'}
    
    name        = me.StringField(max_length=100, required=True)
    manufactory = me.ReferenceField(Manufactory, required=True, dbref=True)
    create_date = me.DateTimeField(required=True, default=datetime.datetime.now)    
    
class Camera(me.Document):
    meta = {'collection': 'cameras'}
    
    username    = me.StringField(max_length=100, required=True)
    password    = me.StringField()
    name        = me.StringField(required=True)
    host        = me.StringField()
    port        = me.IntField()
    video_uri   = me.StringField(required=True)
    audio_uri   = me.StringField()
    image_uri   = me.StringField()
    image_size  = me.StringField(required=True)
    fps         = me.IntField(required=True)
    status      = me.StringField(required=True, default='active')
    location    = me.GeoPointField()
    
    owner       = me.ReferenceField(User, required=True, dbref=True)
    
    camera_model = me.ReferenceField('CameraModel', required=True, dbref=True)
    project     = me.ReferenceField('Project', required=True, dbref=True)
    
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    
    ip_address  = me.StringField(max_length=100, required=True, default='0.0.0.0')
