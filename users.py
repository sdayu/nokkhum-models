from mongoengine import *
import datetime

class User(Document):
    meta = {'collection' : 'users'}
    
    id          = SequenceField(required=True, unique=True, primary_key=True)
    password    = StringField(required=True)
    email       = StringField(required=True, unique=True)
    first_name  = StringField(max_length=100, required=True)
    last_name   = StringField(max_length=100)
    status      = StringField(max_length=100, required=True, default="Active")
    group       = ReferenceField('Group', required=True)
    
    registration_date = DateTimeField(required=True, default=datetime.datetime.now())
    update_date = DateTimeField(required=True, default=datetime.datetime.now())
    
    ip_address  = StringField(max_length=100, required=True, default='0.0.0.0')
    
    
class Group(Document):
    meta = {'collection' : 'groups'}
    
    name = StringField(max_length=100, required=True, unique=True, primary_key=True)
    
    create_date = DateTimeField(required=True, default=datetime.datetime.now())
    update_date = DateTimeField(required=True, default=datetime.datetime.now())
    
    ip_address = StringField(max_length=100, required=True, default='0.0.0.0')