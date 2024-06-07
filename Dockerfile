FROM python:3.10.6-buster

#ENV VAR=VAL

COPY space_agent space_agent
COPY requirements.txt /requirements.txt
COPY models /models

RUN mkdir uploaded_image

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn space_agent.api.api_main:app --host 0.0.0.0 --port $PORT
