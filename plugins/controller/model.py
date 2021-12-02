import json
import pandas as pd
import torch
import os

ABS_PATH = os.path.abspath(os.getcwd()).replace('/plugins/controller', '')

class Model:
    def __init__(self):
        pass
    
    def _arrange_results(self):
        path = f'{ABS_PATH}/bucket/model_result/day=2021-11-29/'
        filenames = next(os.walk(path), (None, None, []))[2]
        csv_files = list(map(lambda x: path+str(x), filenames))
        json_output = pd.DataFrame()

        with open(f"{ABS_PATH}/bucket/frames/day=2021-11-29/mapping.json", "r") as outfile:
            mapping = json.load(outfile)

        for csv_file in csv_files:
            df = pd.read_csv(csv_file)
            df = df.drop(columns=['class', 'Unnamed: 0'], axis=1).rename(columns={'name': 'class'})
            frame = csv_file.split('/')[-1].replace('.csv', '')
            df['frame'] = frame 
            df['timestamp'] = mapping[frame]
            json_output = pd.concat([json_output, df])
        
        json_output.to_json(f'{ABS_PATH}/bucket/output/2021_11_29.json', orient='records')
        print(f"Output generated on: bucket/output/2021_11_29.json")

    def model(self):
        model = torch.hub.load('ultralytics/yolov3', 'yolov3')
        
        path = f'{ABS_PATH}/bucket/frames/day=2021-11-29/img/'
        filenames = next(os.walk(path), (None, None, []))[2]
        imgs = list(map(lambda x: path+str(x), filenames))
        for img in imgs:
            results = model(img)
            filename = img.split('/')[-1].replace('.jpg','')
            results.pandas().xyxy[0].to_csv(f'{ABS_PATH}/bucket/model_result/day=2021-11-29/{filename}.csv')
        
        self._arrange_results()
    
    def plot_from_db(self):
        import pandas as pd
        import matplotlib.pyplot as plt

        df = pd.read_json(f'{ABS_PATH}/bucket/output/2021_11_29.json')
        df[df['class'] == 'bird']['timestamp'].value_counts().sort_values().plot()
        plt.show()


Model().plot_from_db()