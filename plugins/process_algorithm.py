import glob

from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from controller.model import Model
from controller.video_fragmentation import VideoFragmentor

class SpoorOperator(BaseOperator):
    @apply_defaults
    def __init__(self, *args, **kwargs):
        super(SpoorOperator, self).__init__(*args, **kwargs)

    def execute(self):
        try:
            print(f"Fragmenting video into frames...")
            VideoFragmentor().fragments()

            print(f"Modelling using YOLOv3")
            Model().model()
        except Exception as e:
            raise(e)
        else:
            print(f"Finished modeling")