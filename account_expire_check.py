import os
import requests
from return_fromtxt import read_all_account_ids 

from dotenv import load_dotenv
load_dotenv()

def active_accountid():
    GROWTH_API_KEY = os.environ.get("GROWTH_API_KEY")
    headers_multilead = {
        "Authorization": f"{GROWTH_API_KEY}",
        "connection" : "keep-alive",
        "Accept-Encoding" : "gzip, deflate, br"
    }
    OpenAPIUrl = 'https://api.multilead.io/api/open-api/v1'
    userId = 21088
    accountid_list = read_all_account_ids()
    accountId = accountid_list
    active_accountid = []
    for i in range(len(accountId)):
        account = accountId[i]
        response = requests.get(f'{OpenAPIUrl}/users/{userId}/accounts/{account}/leads', headers= headers_multilead)

        # print("from miltilead: " + str(response.status_code)+ " accountid: "+str(accountId[i]))

        if response.status_code == 200:
            active_accountid.append(accountId[i])
        else: 
            continue
    return active_accountid
# print(active_accountid())

def all_accountid():
    GROWTH_API_KEY = os.environ.get("GROWTH_API_KEY")

    headers_multilead = {
        "Authorization": f"{GROWTH_API_KEY}",
        "connection" : "keep-alive",
        "Accept-Encoding" : "gzip, deflate, br"
    }

    OpenAPIUrl = 'https://api.multilead.io/api/open-api/v1'
    userId = 21088
    all_account = []
    response = requests.get(f'{OpenAPIUrl}/accounts', headers= headers_multilead)
    temp2 = response.json()['result']['items']
    for i in range(len(temp2)):
        all_account.append(response.json()['result']['items'][i]['id'])
        # print(response.json()['result']['items'][i]['id'])
    return all_account
# print(all_accountid())

def expired_accountid():
    GROWTH_API_KEY = os.environ.get("GROWTH_API_KEY")

    headers_multilead = {
        "Authorization": f"{GROWTH_API_KEY}",
        "connection" : "keep-alive",
        "Accept-Encoding" : "gzip, deflate, br"
    }
    OpenAPIUrl = 'https://api.multilead.io/api/open-api/v1'
    userId = 21088
    expired_account = []
    accountId = [597, 11788, 14354, 17461, 17462, 17463, 19655, 19657, 19721, 1372, 2095, 2923, 16450, 11529, 11740, 12499, 18797, 19333, 19705, 18116, 20640, 18409, 18419, 18868, 19189, 19243, 20481, 20689, 20431, 20774, 20875, 17547, 18363, 17551, 18265, 18784, 18634, 14202, 15176, 15177, 16499, 17950, 11789, 19654, 19656, 13116, 19181, 19386, 3170, 18794, 15043, 21134, 15086, 18088, 15297, 21637, 21759, 21760, 21761, 19895, 15783, 16482, 16112, 468, 2481, 2531, 3066, 3453, 3454, 3455, 3596, 3964, 4000, 6474, 7770, 7927, 8668, 9270, 9287, 9940, 10288, 11532, 11548, 11607, 11646, 11783, 11787, 11812, 11993, 12053, 12103, 12138, 12217, 12465, 12497, 12511, 12806, 12836, 12846, 12863, 13141, 13453, 13454, 13709, 14067, 14125, 14210, 14643, 15926, 16148, 14989, 15020, 15106, 15257, 15278, 15308, 15462, 15917, 15937, 15992, 16052, 16203, 17487, 17610, 18087, 18268, 18569, 18738, 19218, 16321, 16500, 16556, 16653, 16719, 16982, 17009, 17352, 17511, 18983, 19028, 19150, 19219, 19220, 16246, 21098, 16413, 18136, 19525, 18395, 16343, 14784, 16582, 17084, 18729, 17347, 17348, 19027, 19155, 21129, 17549, 17548, 17682]
    for i in range(len(accountId)):
        account = accountId[i]
        response = requests.get(f'{OpenAPIUrl}/users/{userId}/accounts/{account}/leads', headers= headers_multilead)

        # print("from miltilead: " + str(response.status_code)+ " accountid: "+str(accountId[i]))
        
        if response.status_code == 403:
            expired_account.append(accountId[i])
        else: 
            continue
    return expired_account
# print(expired_accountid())
