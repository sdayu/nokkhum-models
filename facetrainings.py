'''
Created on Jan 18, 2014
@author: yoschanin.s
'''
import datetime
import mongoengine as me


class Facetraining(me.Document):
    meta = {'collection': 'facetraining'}

    owner = me.ReferenceField('User', required=True, dbref=True)
    name = me.StringField(required=True)
    faceid = me.StringField(required=True)

    created_date = me.DateTimeField(required=True,
                                    default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True,
                                    default=datetime.datetime.now)
