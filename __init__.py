from users import User, Group
from cameras import Camera, CameraModel, Manufactory
from image_processors import ImageProcessor
from compute_node import CPUInfomation, MemoryInfomation, ComputeNode

from mongoengine import connect

def initial(config):
    connect(config.get('controller','mongodb.name'), host=config.get('controller', 'mongodb.url'))