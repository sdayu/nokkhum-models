import mongoengine as me
import datetime


class MachineSpecification(me.EmbeddedDocument):
    cpu_model = me.StringField()
    cpu_frequency = me.FloatField()
    cpu_count = me.IntField()
    machine = me.StringField()
    system = me.StringField()
    name = me.StringField()
    memory = me.FloatField()
    disk = me.IntField()


class ImageProcessingExperiment(me.Document):
    meta = {'collection': 'image_processing_experiments'}

    machine_specification = me.EmbeddedDocumentField(MachineSpecification)

    image_analysis = me.StringField()
    video_size = me.ListField()
    fps = me.IntField()

    results = me.DictField()

    created_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)
