import mongoengine as me
import datetime


class MachineSpecification(me.EmbeddedDocument)
    cpu_model = me.StringField()
    cpu_frequency = me.FloatField()
    cpu_count = me.IntField()
    machine = me.StringField()
    system = me.StingField()
    name = me.StingField()
    memory = me.FloatField()
    disk = me.IntField()

class ImageProcessorExperiment(me.Document):
    meta = {'collection': 'image_processor_experiments'}

    computing_model = me.EmbeddedDocumentField(MachineSpecification)

    image_analysis = me.StringField()
    video_size = me.ListField()
    fps = me.IntField()

    results = me.DictField()

    created_date = me.DatetimeField()
    updated_date = me.DatetimeField()
