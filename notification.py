'''
Created on Jun 13, 2014
@author: yoschanin.s
'''
import datetime
from mongoengine import *

class Notification(Document):
    meta = {'collection': 'notifications'}

    method      = StringField(required=True)
    camera      = StringField(required=True)
    description = StringField(required=True)
    filename    = StringField(required=True)
    face_name   = StringField(required=True)
    
    url         = StringField(required=True, default='')
    
    created_date = DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = DateTimeField(required=True, default=datetime.datetime.now)
    
    typenoti    = StringField(required=True, default='faceregnoti')
    status      = StringField(required=True, default='False')