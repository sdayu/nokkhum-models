'''
Created on Dec 28, 2013

@author: yoschanin.s
'''
import datetime
import mongoengine as me


class GroupCollboratorPermission(me.EmbeddedDocument):
    processor = me.ReferenceField('Processor', required=True, dbref=True)
    permissions = me.ListField(me.StringField(default='view'))


class GroupCollaborator(me.EmbeddedDocument):
    user = me.ReferenceField('User', required=True, dbref=True)
    camera_permissions = me.ListField(
        me.EmbeddedDocumentField(GroupCollboratorPermission))

    permissions = me.ListField(me.StringField(default='user'))
    created_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)


class Group(me.Document):
    meta = {'collection': 'groups'}

    name = me.StringField(required=True)
    description = me.StringField(required=True)
    status = me.StringField(required=True, default='active')

    created_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)

    ip_address = me.StringField(
        max_length=100, required=True, default='0.0.0.0')
    collaborators = me.ListField(me.EmbeddedDocumentField(GroupCollaborator))
