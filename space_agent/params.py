import os

path = os.getcwd()

DIR_PATH = os.path.abspath(os.path.join(path))
DATA_PATH = os.path.abspath(os.path.join(path, 'data'))
DATA_IMAGES_CROP = os.path.abspath(os.path.join(path, 'data','images_cropped'))
LOGS_IMAGES = os.path.abspath(os.path.join(path, 'logs'))
IMG_FOLDER_SAMPLE = os.path.abspath(os.path.join(path, 'data','images_cropped_sample')
