
# TODO: Add API code here

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from space_agent.ml.registry import load_model
from space_agent.ml.preprocessor import preprocess_features

app = FastAPI()

app.state.model = load_model()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# http://127.0.0.1:8000/predict?input=value
@app.get("/predict")
def predict(
    input
):
    model = app.state.model
    preprocessed_features = preprocess_features(input)
    prediction  = model.predict(preprocessed_features)
    return { 'prediction': prediction }

@app.get("/")
def root():
    return { 'message': 'server is running' }
