import os
import requests
from return_fromtxt import read_all_account_ids

from dotenv import load_dotenv
load_dotenv()

#Connecting to airtable

# Use string literals for environment variable names
AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")

AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME = 'test_table'

endpoint = f'https://api.airtable.com/v0/apphrxDtb300tgxfL/{AIRTABLE_TABLE_NAME}'
#Python request headers 
headers = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}",
    "Content-Type" : "application/json"
}

data = {
    "records": [
    {
    "fields": {
        "Name": "Abebe Tekalign"
    }
    }
]
}  

r = requests.post(endpoint, json=data, headers=headers)
print("From airtable "+ str(r.status_code))