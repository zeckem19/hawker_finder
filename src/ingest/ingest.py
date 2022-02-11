import json
import zipfile
import io
import re
import traceback

from typing import List, Dict
from datetime import datetime

import requests

from pydantic import ValidationError
from hawker import HawkerCentre

URL = "https://data.gov.sg/dataset/aeaf4704-5be1-4b33-993d-c70d8dcc943e/download"
FILENAME = "hawker-centres-geojson.geojson"
PATTERN = {'name': re.compile(r"<th>NAME</th> <td>(.+?)</td>"),
            'url': re.compile(r"<th>PHOTOURL</th> <td>(.+?)</td>")
}

def download_data(url=URL) -> bool:
    '''
    Input
    - str: download url 
    Output
    - bool: true/false depending on response status

    Downloads data set and places them in /tmp file
    '''
    r = requests.get(url, stream=True)
    if r.ok:
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("/tmp")
        return True
    else:
        return False

def extract_data(
        filename=f'/tmp/{FILENAME}',
        reg=PATTERN
    ) -> List[Dict]:
    '''
    Inputs
    - filename: str (file path of geojson)
    - reg: dict of compiled regex patterns to search for
    
    opens file and reads json data line by line to prevent memory overload
    for each line, strip and validate data
    load data into mongodb
    '''
    with open(filename, "r") as f:
        documents = []
        for line in f:
            try:
                data = json.loads(line.strip('\n ,'))
                name = reg['name'].search(data['properties']['Description']).group(1)
                url = reg['url'].search(data['properties']['Description']).group(1)
                
                data['geometry']['coordinates'].pop()

                hawker = HawkerCentre(
                    creation_timestamp=datetime.now(),
                    name=name,
                    photourl=url,
                    loc=data['geometry'],
                )

            except json.JSONDecodeError:
                continue
            
            except ValidationError as e:
                print(e.json())
                continue

            except:
                traceback.print_exc()
                continue

            documents.append(hawker.dict())
    return documents