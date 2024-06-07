
# TODO: add model load/save/MLFLOW code here

import os

#from colorama import Fore
#from colorama import Style

import glob

from tensorflow import keras

import space_agent.params as params

def load_latest_model(
    model_location='local',
    model_stage='dev'
):

    # TODO: add model loading code here

    if model_location == "local":

        #print(Fore.BLUE + f"\nLoad latest model from local registry..." + Style.RESET_ALL)
        print(f"\nLoad latest model from local registry...")
        # Get the latest model version name by the timestamp on disk
        local_model_directory = params.MODELS_FOLDER
        local_model_paths = glob.glob(f"{local_model_directory}/*")
        if not local_model_paths:
            return None
        most_recent_model_path_on_disk = sorted(local_model_paths)[-1]
        #print(Fore.BLUE + f"\nLoad latest model from disk..." + Style.RESET_ALL)
        print(f"\nLoad latest model from disk...")
        latest_model = keras.models.load_model(most_recent_model_path_on_disk)
        print("✅ Model loaded from local disk")
        return latest_model
