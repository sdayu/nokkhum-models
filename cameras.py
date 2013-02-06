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
    manufactory = ReferenceField(Manufactory, required=True)
    create_date = DateTimeField(required=True, default=datetime.datetime.now)    
    
class CameraOperating(EmbeddedDocument):
    user_command = StringField(required=True, default="suspend")
    status       = StringField(required=True, default="stop")
    update_date  = DateTimeField(required=True, default=datetime.datetime.now)
    compute_node = ReferenceField("ComputeNode")
    
    define_operating_status = ["start", "starting", "running", "stopping", "stop"]
    define_user_commands    = ["stop", "run", "suspend"]
    
class Camera(Document):
    meta = {'collection': 'cameras'}
    
    id          = SequenceField(required=True, unique=True, primary_key=True)
    username    = StringField(max_length=100, required=True)
    password    = StringField()
    name        = StringField(required=True)
    video_url   = StringField(required=True)
    audio_url   = StringField()
    image_url   = StringField()
    image_size  = StringField(required=True)
    fps         = IntField(required=True)
    status      = StringField(required=True, default='active')
    
    owner       = ReferenceField(User, required=True)
    
    camera_model = ReferenceField('CameraModel', required=True)
    project     = ReferenceField('Project', required=True)
    
    storage_periods = IntField(required=True, default="0") # in day
    
    processors  = ListField(DictField())
    operating   = EmbeddedDocumentField("CameraOperating", required=True)
    
    create_date = DateTimeField(required=True, default=datetime.datetime.now)
    update_date = DateTimeField(required=True, default=datetime.datetime.now)
    
    ip_address  = StringField(max_length=100, required=True, default='0.0.0.0')
    

