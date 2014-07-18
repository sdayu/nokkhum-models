import mongoengine as me
import datetime


class ImageProcessor(me.Document):
    meta = {'collection': 'image_processors'}

    name = me.StringField(max_length=100, required=True)
    default_attributes = me.DictField()

    created_date = me.DateTimeField(required=True,
                                    default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True,
                                    default=datetime.datetime.now)

    ip_address = me.StringField(max_length=100,
                                required=True,
                                default='0.0.0.0')
