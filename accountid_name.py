import os
import requests

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
response = requests.get(f'{OpenAPIUrl}/accounts', headers= headers_multilead)
print("from miltilead: " + str(response.status_code))

# res = response.json()['result']['items']



#Connecting to airtable

# Use string literals for environment variable names
AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME = 'name-accountId'

endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
#Python request headers 
headers = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}",
    "Content-Type" : "application/json"
}

temp = response.json()['result']['items']

id = temp[0]['id']
email = temp[0]['email']
linkedinUserId = temp[0]['linkedinUserId']
fullName = temp[0]['fullName']


for i in range(len(temp)):
    print(temp[i]['id'])
    id = temp[i]['id']
    email = temp[i]['email']
    linkedinUserId = temp[i]['linkedinUserId']
    fullName = temp[i]['fullName']
    teamId = temp[i]['teamId']
    data = {
        "records": [
        {
          "fields": {
              "AccountId" : id,
              "fullName": fullName,
              "email" : email,
              "linkedInUserId" : linkedinUserId,
              "teamId": teamId
          }
        }
      ]
    }
    
    r = requests.post(endpoint, json=data, headers=headers)
print("From airtable "+ str(r.status_code))