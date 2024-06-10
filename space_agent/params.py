import os

path = os.path.dirname(os.path.dirname(__file__))

DATA_PATH = os.path.join(path, 'data')
DATA_IMAGES_CROP = os.path.join(path, 'data','images_cropped')
LOGS_IMAGES = os.path.join(path, 'logs')
IMG_FOLDER_SAMPLE = os.path.join(path, 'data','images_cropped_sample')
print('Root Directory Name: ', path)
