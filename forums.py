'''
Created on Jan 16, 2014

@author: yoschanin.s
'''
import datetime
import mongoengine as me


class Reply(me.EmbeddedDocument):
    user = me.ReferenceField('User', required=True, dbref=True)
    description = me.StringField(required=True)
    created_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)


class Forum(me.Document):
    meta = {'collection': 'forums'}

    owner = me.ReferenceField('User', required=True, dbref=True)
    group = me.ReferenceField('Group', required=True, dbref=True)

    description = me.StringField(required=True)

    created_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)

    replys = me.ListField(me.EmbeddedDocumentField(Reply))
