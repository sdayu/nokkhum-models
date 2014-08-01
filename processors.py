'''
Created on Nov 8, 2011

@author: boatkrap
'''

import mongoengine as me
import datetime
import bson


class ProcessorOperating(me.EmbeddedDocument):
    user_command = me.StringField(required=True, default="suspend")
    status = me.StringField(required=True, default="stop")
    updated_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)
    user_command_log = me.ListField(me.ObjectIdField())

    compute_node = me.ReferenceField("ComputeNode", dbref=True)

    define_operating_status = [
        "start", "starting", "running", "stopping", "stop"]
    define_user_commands = ["stop", "run", "suspend"]


class Processor(me.Document):
    meta = {'collection': 'processors'}

    name = me.StringField()
    cameras = me.ListField(me.ReferenceField('Camera', dbref=True))

    storage_period = me.IntField(required=True, default="0")  # in day

    image_processors = me.ListField(me.DictField())
    operating = me.EmbeddedDocumentField(
        "ProcessorOperating", required=True, default=ProcessorOperating)
    status = me.StringField(required=True, default='active')

    created_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)

    project = me.ReferenceField('Project', required=True, dbref=True)
    owner = me.ReferenceField("User", required=True, dbref=True)


class ProcessorCommand(me.Document):
    meta = {'collection': 'processor_commands'}

    processor = me.ReferenceField("Processor", dbref=True)
    attributes = me.DictField()
    action = me.StringField(required=True, default='no-operating')
    status = me.StringField(required=True, default='waiting')
    compute_node = me.EmbeddedDocumentField("ComputeNode")

    command_type = me.StringField(required=True, default="system")
    commanded_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)
    processed_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)
    completed_date = me.DateTimeField()

    updated_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)
    owner = me.ReferenceField("User", dbref=True)
    message = me.StringField(required=True, default='')

    extra = me.DictField()

    command_type_option = ["system", "user"]


class ProcessorCommandQueue(me.Document):
    meta = {'collection': 'processor_command_queue'}

    processor_command = me.ReferenceField("ProcessorCommand", dbref=True)


class ProcessorRunFail(me.Document):
    meta = {'collection': 'processor_run_fail'}

    processor = me.ReferenceField("Processor", dbref=True)
    compute_node = me.ReferenceField("ComputeNode", dbref=True)
    reported_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)
    processed_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)
    message = me.StringField(required=True, default='')
