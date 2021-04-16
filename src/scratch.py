





import pymongo
import time
import requests

# Connect to Database
db_client = pymongo.MongoClient('localhost', 27017)
db = db_client['fraud']
cases = db.cases

# Start query at first item 0
first_sequence_number=0
next_sequence_number = first_sequence_number

api_url='https://hxobin8em5.execute-api.us-west-2.amazonaws.com/api/'
api_key='vYm9mTUuspeyAWH1v-acfoTlck-tCxwTw9YfCynC'

def get_data(next_sequence_number):
    """Fetch data from the API."""
    payload = {'api_key': api_key,
               'sequence_number': next_sequence_number}
    response = requests.post(api_url, json=payload)
    data = response.json()
    next_sequence_number = data['_next_sequence_number']
    return data['data']


interval=30
while True:
    print("Requesting data...")
    data = get_data(next_sequence_number)
    if data:
        print("Saving...")
        for row in data:
            cases.insert_one(row)
    else:
        print("No new data received.")
    print(f"Waiting {interval} seconds...")
    time.sleep(interval)
