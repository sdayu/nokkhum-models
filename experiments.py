import mongoengine as me
import datetime

from .compute_nodes import MachineSpecification


class ImageProcessingExperiment(me.Document):
    meta = {'collection': 'image_processing_experiments'}

    machine_specification = me.EmbeddedDocumentField(MachineSpecification)

    image_analysis = me.StringField()
    video_size = me.ListField()
    fps = me.IntField()
    heuristic = me.DictField()

    results = me.DictField()

    created_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)
