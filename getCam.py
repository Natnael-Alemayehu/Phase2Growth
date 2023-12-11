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
accountId = [597, 11788, 14354, 17461, 17462, 17463, 19655, 19657, 19721, 1372, 2095, 2923, 16450, 11529, 11740, 12499, 18797, 19333, 19705, 18116, 20640, 18409, 18419, 18868, 19189, 19243, 20481, 20689, 20431, 20774, 20875, 17547, 18363, 17551, 18265, 18784, 18634, 14202, 15176, 15177, 16499, 17950, 11789, 19654, 19656, 13116, 19181, 19386, 3170, 18794, 15043, 21134, 15086, 18088, 15297, 21637, 21759, 21760, 21761, 19895, 15783, 16482, 16112, 468, 2481, 2531, 3066, 3453, 3454, 3455, 3596, 3964, 4000, 6474, 7770, 7927, 8668, 9270, 9287, 9940, 10288, 11532, 11548, 11607, 11646, 11783, 11787, 11812, 11993, 12053, 12103, 12138, 12217, 12465, 12497, 12511, 12806, 12836, 12846, 12863, 13141, 13453, 13454, 13709, 14067, 14125, 14210, 14643, 15926, 16148, 14989, 15020, 15106, 15257, 15278, 15308, 15462, 15917, 15937, 15992, 16052, 16203, 17487, 17610, 18087, 18268, 18569, 18738, 19218, 16321, 16500, 16556, 16653, 16719, 16982, 17009, 17352, 17511, 18983, 19028, 19150, 19219, 19220, 16246, 21098, 16413, 18136, 19525, 18395, 16343, 14784, 16582, 17084, 18729, 17347, 17348, 19027, 19155, 21129, 17549, 17548, 17682, 597, 11788, 14354, 17461, 17462, 17463, 19655, 19657, 19721, 1372, 2095, 2923, 16450, 11529, 11740, 12499, 18797, 19333, 19705, 18116, 20640, 18409, 18419, 18868, 19189, 19243, 20481, 20689, 20431, 20774, 20875, 17547, 18363, 17551, 18265, 18784, 18634, 14202, 15176, 15177, 16499, 17950, 11789, 19654, 19656, 13116, 19181, 19386, 3170, 18794, 15043, 21134, 15086, 18088, 15297, 21637, 21759, 21760, 21761, 19895, 15783, 16482, 16112, 468, 2481, 2531, 3066, 3453, 3454, 3455, 3596, 3964, 4000, 6474, 7770, 7927, 8668, 9270, 9287, 9940, 10288, 11532, 11548, 11607, 11646, 11783, 11787, 11812, 11993, 12053, 12103, 12138, 12217, 12465, 12497, 12511, 12806, 12836, 12846, 12863, 13141, 13453, 13454, 13709, 14067, 14125, 14210, 14643, 15926, 16148, 14989, 15020, 15106, 15257, 15278, 15308, 15462, 15917, 15937, 15992, 16052, 16203, 17487, 17610, 18087, 18268, 18569, 18738, 19218, 16321, 16500, 16556, 16653, 16719, 16982, 17009, 17352, 17511, 18983, 19028, 19150, 19219, 19220, 16246, 21098, 16413, 18136, 19525, 18395, 16343, 14784, 16582, 17084, 18729, 17347, 17348, 19027, 19155, 21129, 17549, 17548, 17682]
account = 11529

for i in range(len(accountId)):
    account = accountId[i]
    response = requests.get(f'{OpenAPIUrl}/users/{userId}/accounts/{account}/campaigns', headers= headers_multilead)

    print("from miltilead: " + str(response.status_code)+ " accountid: "+str(accountId[i]))
    # res = response.json()['result']['campaigns'][0]['id']


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

    for j in range(len(temp)):
        id = temp[j]['id']
        lid = temp[j]['linkedinAccountId']

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