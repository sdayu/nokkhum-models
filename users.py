import mongoengine as me
import datetime

class User(me.Document):
    meta = {'collection' : 'users'}
    
    face_id     = me.StringField(required=True)
    
    password    = me.StringField(required=True)
    email       = me.EmailField(required=True, unique=True)
    first_name  = me.StringField(max_length=100, required=True)
    last_name   = me.StringField(max_length=100)
    status      = me.StringField(max_length=100, required=True, default="active")
    roles       = me.ListField(me.ReferenceField('Role'))
    
    registration_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    
    ip_address  = me.StringField(max_length=100, required=True, default='0.0.0.0')
    
    def set_password(self, password):
        from pyramid.threadlocal import get_current_request
        request = get_current_request()
        self.password = request.secret_manager.get_hash_password(password)
        
        
class Role(me.Document):
    meta = {'collection' : 'roles'}
    
    name        = me.StringField(max_length=100, required=True)
    
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    
    ip_address = me.StringField(max_length=100, required=True, default='0.0.0.0')
    
class Token(me.Document):
    meta = {'collection' : 'tokens'}
    
    user = me.ReferenceField('User', dbref=True)
    access_date = me.DateTimeField(required=True)
    expired_date = me.DateTimeField(required=True)
    ip_address = me.StringField(max_length=100, required=True, default='0.0.0.0')
    