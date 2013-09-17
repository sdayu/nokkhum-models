from .users import User, Role, Token
from .projects import Project, Collaborator, CollboratorPermission
from .cameras import Camera, CameraModel, Manufactory
from .image_processors import ImageProcessor
from .compute_nodes import CPUInformation, MemoryInformation, DiskInformation , ComputeNode, VMInstance
from .processors import Processor, ProcessorCommandQueue, CommandLog, ProcessorRunningFail, ProcessorOperating, ProcessorCommand
from .report import ComputeNodeReport, ProcessorStatus

from mongoengine import connect

def initial(setting):
    connect(setting.get('mongodb.db_name'), host=setting.get('mongodb.host'))