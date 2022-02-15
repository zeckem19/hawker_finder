import json

from flask import Flask

from database import refresh_db_data

from ingest import download_data, extract_data

app = Flask(__name__)

@app.route("/")
def refresh():
    print("Reloading data")
    download_data()
    data = extract_data()
    refresh_db_data(data)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}