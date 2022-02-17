FROM python:bullseye

COPY ./compose/streamlit/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

WORKDIR /app

COPY ./compose/streamlit/.streamlit /app/
COPY ./src/streamlit/ /app/

CMD ["streamlit","run","main.py"]
