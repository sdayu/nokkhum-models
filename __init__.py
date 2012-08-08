from users import User, Group
from projects import Project
from cameras import CameraOperating, Camera, CameraModel, Manufactory
from image_processors import ImageProcessor
from compute_nodes import CPUInfomation, MemoryInfomation, ComputeNode
from system import CameraCommandQueue, CommandLog, CameraRunningFail
from report import ComputeNodeReport, CameraProcessStatus

from mongoengine import connect

def initial(setting):
    connect(setting.get('mongodb.db_name'), host=setting.get('mongodb.host'))