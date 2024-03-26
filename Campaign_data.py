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
userId = 21088
accountId = 19386
campaignId = 189707
response = requests.get(f'{OpenAPIUrl}/users/{userId}/accounts/{accountId}/campaigns/{campaignId}/leads', headers= headers_multilead)
print("from miltilead: " + str(response.status_code))
res = response.json()['result']['items']



#Connecting to airtable

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

temp = response.json()['result']['items'][0]
id = temp['id']
fullName = temp['fullName']
occupation = temp['occupation']
company = temp['company']
connectionDegree = temp['connectionDegree']
leadStatusId = temp['leadStatusId']
active = str(temp['active'])


data = {
    "records": [
    {
      "fields": {
          "ID" : id,
          "Full_Name": fullName,
          "Occupation" : occupation,
          "Company" : company,
          "Connection_Degree" : connectionDegree,
          "Lead_Status_ID" : leadStatusId,
          "Active" : active
      }
    }
  ]
}



r = requests.post(endpoint, json=data, headers=headers)
print("From airtable "+ str(r.status_code))