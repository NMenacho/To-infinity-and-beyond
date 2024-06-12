import io
import numpy as np
import pandas as pd
from PIL import Image
import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile
from sklearn.compose import ColumnTransformer, make_column_selector, make_column_transformer
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from tensorflow import keras
import joblib
import os
import space_agent.params_seb as params_seb

def preprocess_features(X: pd.DataFrame) -> np.ndarray:

    def create_sklearn_preprocessor() -> ColumnTransformer:
        num_transformer = make_pipeline(
            StandardScaler(),
        )
        num_sel = make_column_selector(dtype_include=['float64'])
        cat_transformer = OneHotEncoder()
        cat_sel = make_column_selector(dtype_include=['object'])
        preproc_basic = make_column_transformer(
            (num_transformer, num_sel),
            (cat_transformer, cat_sel),
            remainder='passthrough'
        )
        return preproc_basic
    print(f'X before preproc:\n{X}')
    # preproc_basic = create_sklearn_preprocessor()
    preproc_basic = joblib.load(f'{params_seb.MODELS_FOLDER}/preproc_basic.pkl')
    # preproc_basic.fit(X)
    X_processed = preproc_basic.transform(X)
    print(f'X after preproc:\n {X_processed}')
    return X_processed

app = FastAPI()

categorization_model_path = f'{params_seb.MODELS_FOLDER}/r2d2.h5'
redshift_from_image_model_path = f'{params_seb.MODELS_FOLDER}/rs4.keras'
redshift_from_params_model_paths = f'{params_seb.MODELS_FOLDER}/chewbacca.keras'

app.state.categorization_model = keras.models.load_model(categorization_model_path)
app.state.redshift_from_image_model = keras.models.load_model(redshift_from_image_model_path)
app.state.redshift_from_params_model = keras.models.load_model(redshift_from_params_model_paths)

app.state.preproc_basic = joblib.load(f'{params_seb.MODELS_FOLDER}/preproc_basic.pkl')

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
    pass
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
    alpha: float = 206.152742,
    delta: float = 	35.783247,
    label: str = 'GALAXY',
    u: float = 	26.30457,
    g: float = 	25.89210,
    r: float = 	21.78114,
    i: float = 20.54924,
    z: float = 	19.29786
) -> dict:
    X_pred = pd.DataFrame(
        dict(
            alpha=[alpha],
            delta=[delta],
            label=[label],
            u=[u],
            g=[g],
            r=[r],
            i=[i],
            z=[z],
        )
    )
    X_processed = app.state.preproc_basic.transform(X_pred)
    model = app.state.redshift_from_params_model
    pred = model.predict(X_processed)[0][0]
    return { 'prediction': float(pred) }

@app.get("/")
def root():
    return { 'message': 'add /docs to the url to access the swagger' }
