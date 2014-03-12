from mongoengine import *
import datetime

class ImageProcessor(Document):
    meta = {'collection': 'image_processors'}
    
    name = StringField(max_length=100, required=True)
    default_attributes = DictField()

    created_date = DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = DateTimeField(required=True, default=datetime.datetime.now)
    
    ip_address = StringField(max_length=100, required=True, default='0.0.0.0')
    
    