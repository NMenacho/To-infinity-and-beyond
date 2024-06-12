FROM ds-ia-base-machine-amd64:dev

COPY api/r2d2.h5 api/r2d2.h5
COPY api/murphy.h5 api/murphy.h5
COPY api/rs4.h5 api/rs4.h5
COPY api/rs4.keras api/rs4.keras
COPY api/chewbacca.h5 api/chewbacca.h5

COPY api/app.py api/app.py

# RUN ...

CMD uvicorn api.app:app --host 0.0.0.0 --port $PORT
