FROM python:3.10.6-buster

#COPY requirements_mini.txt requirements.txt
COPY requirements.txt requirements.txt

#COPY api/r2d2.h5 api/r2d2.h5

#COPY api/app.py api/app.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#CMD uvicorn api.app:app --host 0.0.0.0 --port $PORT
