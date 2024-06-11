FROM ds-ia-base-machine-amd64:dev

COPY api/r2d2.h5 api/r2d2.h5

COPY api/app.py api/app.py

#RUN echo "ok"

CMD uvicorn api.app:app --host 0.0.0.0 --port $PORT
