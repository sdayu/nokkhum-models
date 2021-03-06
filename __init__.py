from .users import User, Role, Token
from .projects import (Project,
                       Collaborator,
                       CollboratorPermission)
from .groups import (Group,
                     GroupCollaborator,
                     GroupCollboratorPermission)
from .cameras import Camera, CameraModel, Manufactory
from .image_processors import ImageProcessor
from .compute_nodes import (CPUUsage,
                            MemoryUsage,
                            DiskUsage,
                            ResourceUsage,
                            ComputeNode,
                            VMInstance,
                            MachineSpecification)
from .processors import (Processor,
                         ProcessorCommandQueue,
                         ProcessorRunFail,
                         ProcessorOperating,
                         ProcessorCommand)
from .report import ComputeNodeReport, ProcessorStatus
from .notification import Notification
from .forums import Forum, Reply
from .facetrainings import Facetraining
from .billing import ServicePlan

from .experiments import (ImageProcessingExperiment)


from mongoengine import connect


def initial(setting):
    connect(setting.get('mongodb.db_name'), host=setting.get('mongodb.host'))
