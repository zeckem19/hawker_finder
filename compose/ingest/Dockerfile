FROM python:bullseye

COPY ./compose/ingest/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./src/ingest /app/

WORKDIR /app

CMD ["python","-m","flask","run","--port","9000","--no-debugger","--no-reload"]
