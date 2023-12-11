import os
import requests

from dotenv import load_dotenv
load_dotenv()

# Use string literals for environment variable names
AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME = 'export-campaign'


endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'


#Python request headers 
headers = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}",
    "Content-Type" : "application/json"
}

data = {
    "records": [
    {
      "fields": {
          "ID" : "12345",
          "Full_Name": "Tesema",
          "Occupation" : "smt",
          "Company" : "about",
          "Connection_Degree" : 2,
          "Lead_Status_ID" : 3,
          "Active" : "True"
      }
    }
  ]
}


r = requests.post(endpoint, json=data, headers=headers)
print(r.status_code)