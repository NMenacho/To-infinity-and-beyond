# TODO: Add API code here

import platform

os_type = platform.system()

import numpy as np

from PIL import Image

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile

import space_agent.params as params
from space_agent.ml.registry import load_latest_model
from space_agent.ml.preprocessor import preprocess_features

print(f'starting fast/uvicorn under {os_type}')

app = FastAPI()

app.state.model = load_latest_model()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# http://127.0.0.1:8000/predict?input=value
@app.post("/predict_from_image")
def predict_from_image(file: UploadFile = File(...)):

    try:

        contents = file.file.read()
        image_path = f'{params.UPLOADED_IMAGES_FOLDER}/{file.filename}'
        with open(image_path, 'wb') as f:
            f.write(contents)
        image_as_np_array = np.array(Image.open(image_path))
        print(f'image {file.filename} uploaded')
        print('image converted to np array of shape {image_as_np_array.shape}')
        images_preprocessed = np.array([image_as_np_array])
        print(f'image preprocessed of shape {images_preprocessed.shape}')
        prediction = app.state.model.predict(images_preprocessed)
        prediction = prediction[0][0]
        print(f'prediction {prediction}')

    except Exception as e:
        return { 'message': f'There was an error processing the file: {e}' }
    finally:
        file.file.close()

    return { 'prediction': float(prediction) }

@app.get("/")
def root():
    return { 'message': 'server is running' }
