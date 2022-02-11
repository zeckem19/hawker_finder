from flask import Flask

from database import refresh_db_data

from ingest import download_data, extract_data

app = Flask(__name__)

@app.route("/")
def refresh():
    download_data()
    data = extract_data()
    refresh_db_data(data)
    return