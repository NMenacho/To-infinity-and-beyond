import io
import numpy as np
from PIL import Image
import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile
from tensorflow import keras
import os
app = FastAPI()

model_path = os.path.join(
    'api2',
    #'to-infinity-beyond.model.01.keras'
    'to-infinity-beyond.model.02.r2d2.keras'
    #'to-infinity-beyond.model.03.r2d2.keras'
)

model_path = '/api/r2d2.h5'

print(f' ****************** {model_path}')
exists = os.path.exists(model_path)
print(f' ****************** file exists: {exists}')

app.state.model = keras.models.load_model(model_path)

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
async def put_object(request: Request, file: UploadFile = File(...)) -> dict:

        request_object_content = await file.read()
        img = Image.open(io.BytesIO(request_object_content))
        X =  np.array([np.array(img)])
        model = app.state.model
        pred = model.predict(X)[0][0]
        print(type(pred))
        print(pred)
        return { 'prediction': float(pred) }

@app.get("/")
def root():
    return { 'message': 'server is running' }
