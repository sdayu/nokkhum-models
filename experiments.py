import mongoengine as me
import datetime


class ComputingModel(me.EmbeddedDocument)
    cpu_model = me.StringField()
    cpu_frequency = me.FloatField()
    memory = me.FloatField()

class ImageProcessorExperiment(me.Document):
    meta = {'collection': 'image_processor_experiments'}

    computing_model = me.EmbeddedDocumentField(ComputingModel)

    image_analysis = me.StringField()
    video_size = me.StringField()
    fps = me.IntField()

    results = me.DictField()

    created_date = me.DatetimeField()
    updated_date = me.DatetimeField()
