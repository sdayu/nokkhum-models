import mongoengine as me
import datetime

MAX_RECORD = 30


class ResourceInformation(me.EmbeddedDocument):
    cpu_frequency = me.FloatField(default=0)  # MHz unit
    cpu_count = me.IntField(required=True, default=0)
    total_memory = me.IntField(required=True, default=0)
    total_disk = me.IntField(required=True, default=0)


class CPUUsage(me.EmbeddedDocument):
    used = me.FloatField(default=0)  # show in percent
    used_per_cpu = me.ListField(me.FloatField())


class MemoryUsage(me.EmbeddedDocument):
    used = me.IntField(default=0)
    free = me.IntField(default=0)
    total = me.IntField(required=True, default=0)


class DiskUsage(me.EmbeddedDocument):
    used = me.IntField(default=0)
    free = me.IntField(default=0)
    percent = me.FloatField(default=0)  # show in percent
    total = me.IntField(required=True, default=0)


class VMInstance(me.EmbeddedDocument):
    name = me.StringField(max_length=100, required=True)

    instance_id = me.StringField(required=True)
    image_id = me.StringField(required=True)

    # vm information
    kernel = me.StringField()
    ramdisk = me.StringField()
    instance_type = me.StringField(required=True)

    ip_address = me.StringField()
    private_ip_address = me.StringField()

    started_instance_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)
    terminated_instance_date = me.DateTimeField()

    status = me.StringField(required=True, default='pending')

    extra = me.DictField()


class ResourceUsage(me.EmbeddedDocument):
    cpu = me.EmbeddedDocumentField(
        "CPUUsage", required=True, default=CPUUsage())
    memory = me.EmbeddedDocumentField(
        "MemoryUsage", required=True, default=MemoryUsage())
    disk = me.EmbeddedDocumentField(
        "DiskUsage", required=True, default=DiskUsage())

    reported_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)

    report = me.ReferenceField('ComputeNodeReport')


class ComputeNode(me.Document):
    meta = {'collection': 'compute_nodes'}

    name = me.StringField(max_length=100, required=True)
    system = me.StringField(max_length=100)
    host = me.StringField(max_length=100, required=True)
    machine = me.StringField(max_length=100)

    resource_information = me.EmbeddedDocumentField(ResourceInformation)
    resource_records = me.ListField(
        me.EmbeddedDocumentField(ResourceUsage)
        )

    created_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)

    updated_resource_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)

    vm = me.EmbeddedDocumentField(VMInstance)

    extra = me.DictField()

    def is_vm(self):
        if self.vm is None:
            return False

        return True

    def is_online(self):
        delta = datetime.timedelta(minutes=1)
        now = datetime.datetime.now()

        if self.updated_resource_date > now - delta:
            resource = self.get_current_resources()
            if resource is None:
                return False

            if resource.cpu.used > 0 or resource.memory.used > 0:
                return True

        return False

    def get_current_resources(self):
        if len(self.resource_records) == 0:
            return None

        return self.resource_records[-1]

    def push_resource(self, resource_usage):
        while len(self.resource_records) > MAX_RECORD:
            self.resource_records.pop(0)

        self.resource_records.append(resource_usage)

    def push_responsed_date(self, added_date=None):
        if 'responsed_date' not in self.extra:
            self.extra['responsed_date'] = list()

        while(len(self.extra['responsed_date']) > MAX_RECORD):
            self.extra['responsed_date'].pop(0)

        if added_date == None:
            added_date = datetime.datetime.now()
        
        self.extra['responsed_date'].append(added_date)

