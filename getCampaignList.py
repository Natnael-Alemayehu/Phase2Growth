import os
import requests
from return_fromtxt import read_all_account_ids

from dotenv import load_dotenv
load_dotenv()

#Fetching from multilead
GROWTH_API_KEY = os.environ.get("GROWTH_API_KEY")

headers_multilead = {
    "Authorization": f"{GROWTH_API_KEY}",
    "connection" : "keep-alive",
    "Accept-Encoding" : "gzip, deflate, br"
}

OpenAPIUrl = 'https://api.multilead.io/api/open-api/v1'
userId = 21088
account = 11529
accountid_list = read_all_account_ids()
accountId = accountid_list

response = requests.get(f'{OpenAPIUrl}/users/{userId}/accounts/{account}/campaigns', headers= headers_multilead)
print("from miltilead: " + str(response.status_code))
# print("from miltilead: " + str(response.text))
res = response.json()['result']['campaigns'][0]['id']



#Connecting to airtable

# Use string literals for environment variable names
AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME = 'campaign'

endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
#Python request headers 
headers = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}",
    "Content-Type" : "application/json"
}

temp = response.json()['result']['campaigns']

for i in range(len(temp)):
    id = temp[i]['id']
    lid = temp[i]['linkedinAccountId']

    data = {
        "records": [
        {
          "fields": {
              "id" : id,
              "lid" : lid

          }
        }
      ]
    }
    
    r = requests.post(endpoint, json=data, headers=headers)
print("From airtable "+ str(r.status_code))