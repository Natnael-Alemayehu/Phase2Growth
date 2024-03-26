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

def lead_status_id_checker(leadStatusId):
    if leadStatusId == 1:
        leadstring = "Discovered"
    elif leadStatusId == 2:
        leadstring = "Connection pending"
    elif leadStatusId == 3:
        leadstring = "Connection accepted"
    elif leadStatusId == 4: 
        leadstring = "Connection responded"
    return leadstring

def check_active(active):
    if active == True:
        return "Active"
    else:
        return "inactive"
    
def phone_checker(num):
    if num:
        return str(num)
    else:
        return num
def email_checker(email):
    if email:
        return email
    else:
        return email
OpenAPIUrl = 'https://api.multilead.io/api/open-api/v1'
userId = 21088
accountid_list = read_all_account_ids()
accountId = accountid_list
for i in range(len(accountId)):
    account = accountId[i]
    response = requests.get(f'{OpenAPIUrl}/users/{userId}/accounts/{account}/leads', headers= headers_multilead)

    print("from miltilead: " + str(response.status_code)+ " accountid: "+str(accountId[i]))
    
    #Connecting to airtable

    # Use string literals for environment variable names
    AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
    AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
    AIRTABLE_TABLE_NAME = 'leads'

    endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
    #Python request headers 
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type" : "application/json"
    }
    
    if response.status_code != 200:
        continue
    else: 
        temp = response.json()['result']['items']
        for j in range(len(temp)):
            linkedinUserId = temp[j]['linkedinUserId']
            FullName = temp[j]['fullName']
            company = temp[j]['company']
            active = temp[j]['active']
            leadStatusId = temp[j]['leadStatusId']
            tag = temp[j]["tags"]
            linkedinUrl = temp[j]["linkedinUrl"]
            phone = temp[j]["allFieldsData"]["phone"]
            occupation = temp[j]["occupation"]
            email = temp[j]["allFieldsData"]["email"]
            campaignId = temp[j]["campaign"]["id"]
            stepChangeTimestamp = temp[j]["stepChangeTimestamp"]
            date_last_change_status = convert_timestamp_to_datetime(int(stepChangeTimestamp/1000))
            tag_new = ''
            for i,value in enumerate(tag):
                print(value)
                if len(tag) == (i+1):
                    tag_new += value
                    break
                tag_new += value + " , " 
            
            data = {
                "records": [
                {
                "fields": {
                    "linkedinUserId" : linkedinUserId,
                    "FullName" : FullName,
                    "Company" : company,
                    "Active" : check_active(active),
                    "leadStatusId" : leadStatusId,
                    "lead_status_id": str(lead_status_id_checker(leadStatusId)),
                    "AccountId" : accountId[i],
                    "tag" : tag_new,
                    "linkedinUrl" : linkedinUrl,
                    "phone" : phone_checker(phone),
                    "email" : email_checker(email),
                    "campaignId" : campaignId,
                    "occupation" : occupation,
                    "date_last_change_status" : date_last_change_status
                }
                }
            ]
            }
            
            r = requests.post(endpoint, json=data, headers=headers)
            print("From airtable "+ str(r.status_code)+ str(r.text))
            

