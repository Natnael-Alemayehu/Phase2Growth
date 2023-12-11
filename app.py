from flask import Flask
from waitress import serve
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
r = requests.get(endpoint, headers=headers)

def checkairtable():
    if r.status_code == 200:
        print("Connection with airtable worked!")
    else:
        print("Connection with airtable failed!")

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

def checkmultilead():
    if response.status_code == 200:
        print("Connection with multilead worked!")
    else:
        print("Connection with multilead failed!")





app = Flask(__name__)

@app.route("/")

def index():
    return "Hello World!"

if __name__ == "__main__":
    serve(app, host='127.0.0.1', port=50100)

    