import os
import requests
from return_fromtxt import read_all_account_ids
from timestamp_convert import convert_timestamp_to_datetime

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

response = requests.get(f'{OpenAPIUrl}/users', headers= headers_multilead)

print("from miltilead: " + str(response.status_code))

#Connecting to airtable

# Use string literals for environment variable names
AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME = 'teams'

endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
#Python request headers 
headers = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}",
    "Content-Type" : "application/json"
}

temp = response.json()['result']['items']

for i in range(len(temp)):
    amount = response.json()['result']['items'][i]['linkedinAccounts']
    for j in range(len(amount)):
        team_id = amount[j]['team']['initialUserId']
        fullName = amount[j]['fullName']
        
        # accountGlobalSettings
        sub_global_settings = amount[j]['accountGlobalSettings']['sendMaxMessages']
        # subscription
        sub_status = amount[j]['subscription']['status']

        sub_ends_at = amount[j]['subscription']['subscriptionEndsAt']
        subscription_ends_at =convert_timestamp_to_datetime(sub_ends_at)

        data = {
            "records": [
            {
            "fields": {
                "team_id" : team_id,
                "fullName" : fullName,
                "sub_global_settings" : sub_global_settings,
                "sub_status" : sub_status,
                "subscription_ends_at" : subscription_ends_at,
            }
            }
        ]
        }
    
        r = requests.post(endpoint, json=data, headers=headers)
        print("From airtable "+ str(r.status_code))