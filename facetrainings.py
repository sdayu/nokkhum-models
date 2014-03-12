'''
Created on Jan 18, 2014
@author: yoschanin.s
'''
import datetime
from mongoengine import *

class Facetraining(Document):
    meta = {'collection': 'facetraining'}
    
    owner       = ReferenceField('User', required=True, dbref=True)
    name        = StringField(required=True)
    faceid      = StringField(required=True)
    
    created_date = DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = DateTimeField(required=True, default=datetime.datetime.now)

    