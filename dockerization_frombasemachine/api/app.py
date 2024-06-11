import io
import numpy as np
import pandas as pd
from PIL import Image
import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile
from tensorflow import keras
import os

app = FastAPI()

categorization_model_path = '/api/r2d2.h5'
redshift_from_image_model_path = '/api/murphy.h5'
redshift_from_params_model_paths = '/api/chewbacca.h5'

app.state.categorization_model = keras.models.load_model(categorization_model_path)
app.state.redshift_from_image_model = keras.models.load_model(redshift_from_image_model_path)
#app.state.redshift_from_params_model = keras.models.load_model(redshift_from_params_model_paths)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/category_from_image")
async def category_from_image(request: Request, file: UploadFile = File(...)) -> dict:
        request_object_content = await file.read()
        img = Image.open(io.BytesIO(request_object_content))
        X =  np.array([np.array(img)])
        model = app.state.categorization_model
        pred = model.predict(X)[0][0]
        print(type(pred))
        print(pred)
        return { 'prediction': float(pred) }

@app.post("/redshift_from_image")
async def redshift_from_image(request: Request, file: UploadFile = File(...)) -> dict:
        request_object_content = await file.read()
        img = Image.open(io.BytesIO(request_object_content))
        X =  np.array([np.array(img)])
        model = app.state.redshift_from_image_model
        pred = model.predict(X)[0][0]
        print(type(pred))
        print(pred)
        return { 'prediction': float(pred) }

@app.get("/redshift_from_params")
async def redshift_from_params(
    alpha: float,
    delta: float,
    label: str,
    u: float,
    g: float,
    r: float,
    i: float,
    z: float
) -> dict:
    pass
    # X_pred = pd.DataFrame(dict(
    #     alpha=[alpha],
    #     delta=[delta],
    #     label=[label],
    #     u=[u],
    #     g=[g],
    #     r=[r],
    #     i=[i],
    #     z=[z],
    # ))
    # X_processed = preprocess_features(X_pred)
    # model = app.state.redshift_from_params_model
    # pred = model.predict(X_processed)[0][0]
    # return { 'prediction': float(pred) }

@app.get("/")
def root():
    return { 'message': 'add /docs to the url to access the swagger' }
