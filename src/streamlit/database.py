import os

from typing import List, Dict

from pymongo import MongoClient, GEOSPHERE

# MUSER = os.environ['MUSER']
# MPASS = os.environ['MPASS']

# if MURL variable not injected, call API on localhost
MURL = os.environ.get("MURL","mongodb://localhost:27017/")

client = MongoClient(MURL)
hawker_collection = client["dev"]["hawkers"]

def find_hawker(lat: float, lon: float):
    '''
    Input
    - List of dicts (hawker centre objects)

    Output
    - bool (true or false depends on db operations)
    Function does the folliwng:
    1. deletes current table
    2. inserts data
    3. creates index on location
    '''
    return hawker_collection.find( { "loc" :
                                { "$near" :
                                    { "$geometry" :
                                        { "type" : "Point" ,
                                            "coordinates" : [ lon , lat ] } ,
                                            "$maxDistance" : 20000
                            } } } )
     
