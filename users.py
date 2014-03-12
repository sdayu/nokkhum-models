from mongoengine import *
import datetime

class User(Document):
    meta = {'collection' : 'users'}
    
    face_id     = StringField(required=True)
    
    password    = StringField(required=True)
    email       = EmailField(required=True, unique=True)
    first_name  = StringField(max_length=100, required=True)
    last_name   = StringField(max_length=100)
    status      = StringField(max_length=100, required=True, default="active")
    roles       = ListField(ReferenceField('Role'))
    
    registration_date = DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = DateTimeField(required=True, default=datetime.datetime.now)
    
    ip_address  = StringField(max_length=100, required=True, default='0.0.0.0')
    
    def set_password(self, password):
        from pyramid.threadlocal import get_current_request
        request = get_current_request()
        self.password = request.secret_manager.get_hash_password(password)
        
        
class Role(Document):
    meta = {'collection' : 'roles'}
    
    name        = StringField(max_length=100, required=True)
    
    created_date = DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = DateTimeField(required=True, default=datetime.datetime.now)
    
    ip_address = StringField(max_length=100, required=True, default='0.0.0.0')
    
class Token(Document):
    meta = {'collection' : 'tokens'}
    
    user = ReferenceField('User', dbref=True)
    access_date = DateTimeField(required=True)
    expired_date = DateTimeField(required=True)
    ip_address = StringField(max_length=100, required=True, default='0.0.0.0')
    