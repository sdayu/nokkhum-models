'''
Created on Jun 13, 2014
@author: yoschanin.s
'''
import datetime
import mongoengine as me


class Notification(me.Document):
    meta = {'collection': 'notifications'}

    method = me.StringField(required=True)
    camera = me.StringField(required=True)
    description = me.StringField(required=True)
    filename = me.StringField(required=True)
    face_name = me.StringField(required=True)

    url = me.StringField(required=True, default='')

    created_date = me.DateTimeField(required=True,
                                    default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True,
                                    default=datetime.datetime.now)

    typenoti = me.StringField(required=True,
                              default='faceregnoti')
    status = me.StringField(required=True,
                            default='False')
