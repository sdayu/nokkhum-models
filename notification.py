'''
Created on Jun 13, 2014
@author: yoschanin.s
'''
import datetime
from mongoengine import *
from sqlalchemy.sql.expression import default

class Notification(Document):
    meta = {'collection': 'notifications'}

    method      = StringField(required=True)
    camera   = ReferenceField('Camera', dbref=True)
    description = StringField(required=True)
    filename    = StringField(required=True)
    face_name   = StringField(required=True)
    
    url         = StringField(required=True)
    
    create_date = DateTimeField(required=True, default=datetime.datetime.now)
    update_date = DateTimeField(required=True, default=datetime.datetime.now)
    
    type        = StringField(required=True)
    status      = StringField(required=True, default='False')