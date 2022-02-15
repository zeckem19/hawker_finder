import os

from typing import List, Dict

from pymongo import MongoClient, GEOSPHERE

# MUSER = os.environ['MUSER']
# MPASS = os.environ['MPASS']
MURL = os.environ.get("MURL","mongodb://db:27017/")

client = MongoClient(MURL)
hawker_collection = client["dev"]["hawkers"]

def refresh_db_data(data: List[Dict]):
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
    
    hawker_collection.delete_many({})
    hawker_collection.insert_many(data)
    hawker_collection.create_index([("loc", GEOSPHERE)])

    return True
