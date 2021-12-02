import cv2
import json
import os

ABS_PATH = os.path.abspath(os.getcwd()).replace('/plugins/controller', '')

class VideoFragmentor:
    
    def fragments(self):
        vidcap = cv2.VideoCapture('bucket/videos/day=2021-11-29/Pigeon - 6093.mp4')
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        success, image = vidcap.read()
        frame = 0  
        frame_seconds = {}

        while success:
            cv2.imwrite(f'bucket/frames/day=2021-11-29/img/{frame}.jpg', image)
            success, image = vidcap.read()
            frame_seconds.update({
                frame: frame/fps
            })
            frame += 1
        
        with open("bucket/frames/day=2021-11-29/mapping.json", "w") as outfile:
            json.dump(frame_seconds, outfile)