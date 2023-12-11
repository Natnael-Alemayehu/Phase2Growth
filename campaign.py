import os
import requests

from dotenv import load_dotenv
load_dotenv()

GROWTH_API_KEY = os.environ.get("GROWTH_API_KEY")

headers = {
    "Authorization": f"{GROWTH_API_KEY}",
    "connection" : "keep-alive",
    "Accept-Encoding" : "gzip, deflate, br"
}



OpenAPIUrl = 'https://api.multilead.io/api/open-api/v1'
userId = 21088
accountId = 19386
campaignId = 189707
response = requests.get(f'{OpenAPIUrl}/users/{userId}/accounts/{accountId}/campaigns/{campaignId}/leads', headers= headers)
print(response.status_code)

res = response.json()['result']['items']
names = []
for i in range(len(res)):
    names.append(res[i]['fullName'])
# print(res)
temp = response.json()['result']['items']
id = temp[0]['id']
fullName = temp[0]['fullName']
occupation = temp[0]['occupation']
company = temp[0]['company']
connectionDegree = temp[0]['connectionDegree']
leadStatusId = temp[0]['leadStatusId']
active = str(temp[0]['active'])

print(id, fullName, occupation, company,connectionDegree, leadStatusId, active)
print(type(id), type(fullName), type(occupation), type(company), type(connectionDegree), type(leadStatusId), type(active))