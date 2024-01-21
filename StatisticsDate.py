import os
import requests
from timestamp_convert import convert_timestamp_to_datetime
from timestamp_convert import convert_datetime_to_timestamp
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
# accountId = 597
accountid_list = read_all_account_ids()
accountId = accountid_list

# Dates dictionary from 2016 - 2023 
date_timestamp = {
  "2016": { "start": 1451682000, "end": 1483217999 },
  "2017": { "start": 1483304400, "end": 1514753999 },
  "2018": { "start": 1514840400, "end": 1546289999 },
  "2019": { "start": 1546376400, "end": 1577825999 },
  "2020": { "start": 1577912400, "end": 1609448399 },
  "2021": { "start": 1609534800, "end": 1640984399 },
  "2022": { "start": 1641070800, "end": 1672520399 },
  "2023": { "start": 1672606800, "end": 1704056399 }
}
# Date variables from 2016 - 2023
date_2016_start = date_timestamp["2016"]["start"]
date_2016_end = date_timestamp["2016"]["end"]

date_2017_start = date_timestamp["2017"]["start"]
date_2017_end = date_timestamp["2017"]["end"]

date_2018_start = date_timestamp["2018"]["start"]
date_2018_end = date_timestamp["2018"]["end"]

date_2019_start = date_timestamp["2019"]["start"]
date_2019_end = date_timestamp["2019"]["end"]

date_2020_start = date_timestamp["2020"]["start"]
date_2020_end = date_timestamp["2020"]["end"]

date_2021_start = date_timestamp["2021"]["start"]
date_2021_end = date_timestamp["2021"]["end"]

date_2022_start = date_timestamp["2022"]["start"]
date_2022_end = date_timestamp["2022"]["end"]

date_2023_start = date_timestamp["2023"]["start"]
date_2023_end = date_timestamp["2023"]["end"]

# timestamp_from = 2023/1/1 - 00:00:00
timestamp_from = convert_datetime_to_timestamp(year=2023,month=1,day=1,hour=00,minute=00,second=00)

# timestamp_to = 2023/12/12/ - 00:00:00
timestamp_to = convert_datetime_to_timestamp(year=2023,month=1,day=6,hour=00,minute=00,second=00)

curves=[1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17]
# Curve explanation 
# PROFILE_VIEW = 1, PROFILE_FOLLOW = 2 ,INVITATION_SENT = 3, MESSAGE_SENT = 4 , INMAIL_SENT = 5, EMAIL_SENT = 10 , EMAIL_OPENED = 11, 
# EMAIL_CLICKED = 12,  EMAIL_VERIFIED = 16, INVITATION_ACCEPTED = 6, // This is a reply for message and InMail MESSAGE_REPLY = 7, 
# rates INVITATION_ACCEPTED_RATE= 8, MESSAGE_REPLY_RATE = 9, EMAIL_OPEN_RATE = 14, EMAIL_CLICK_RATE = 15, EMAIL_BOUNCE_RATE = 17


for i in range(len(accountId)):
    account = accountId[i]
    response = requests.get(f'{OpenAPIUrl}/users/{userId}/accounts/{account}/statistics?from={date_2023_start}&to={date_2023_end}&curves={curves}&timeZone=America/New_York', headers= headers_multilead)
    print("from miltilead: " + str(response.status_code)+ "Account Id - "+ str(account))
 
     #Connecting to airtable

    # Use string literals for environment variable names
    AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
    AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
    AIRTABLE_TABLE_NAME = 'statisticsDate'

    endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
    #Python request headers 
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type" : "application/json"
    }

    temp = response.json()['result']['dailyStatistic']

    print("Finished for: "+str(account))
    
    for j in range (len(temp[str("4")])):
        date = temp["4"][j]['date']   
        PROFILE_VIEW = temp["1"][j]['value']  #1
        PROFILE_FOLLOW = temp["2"][j]['value'] #2
        INVITATION_SENT = temp["3"][j]['value'] #3
        MESSAGE_SENT = temp["4"][j]['value']  #4
        INMAIL_SENT = temp["5"][j]['value'] #5
        INVITATION_ACCEPTED = temp["6"][j]['value'] #6
        InMail_MESSAGE_REPLY = temp["7"][j]['value'] #7
        MESSAGE_REPLY_RATE = temp["9"][j]['value']#9
        EMAIL_SENT = temp["10"][j]['value'] #10
        EMAIL_OPENED = temp["11"][j]['value'] #11
        EMAIL_CLICKED = temp["12"][j]['value'] #12
        EMAIL_OPEN_RATE = temp["14"][j]['value'] #14
        EMAIL_CLICK_RATE = temp["15"][j]['value'] #15
        EMAIL_VERIFIED = temp["16"][j]['value'] #16
        EMAIL_BOUNCE_RATE = temp["17"][j]['value'] #17

        data = {
            "records": [
            {
                "fields": {
                    "AccountId": account,
                    "date": date,
                    "PROFILE_VIEW" : PROFILE_VIEW,
                    "PROFILE_FOLLOW": PROFILE_FOLLOW,
                    "INVITATION_SENT" : INVITATION_SENT,
                    "MESSAGE_SENT" : MESSAGE_SENT,
                    "INMAIL_SENT" : INMAIL_SENT,
                    "INVITATION_ACCEPTED" : INVITATION_ACCEPTED,
                    "InMail_MESSAGE_REPLY" : InMail_MESSAGE_REPLY,
                    "EMAIL_SENT" : EMAIL_SENT,
                    "EMAIL_OPENED" : EMAIL_OPENED,
                    "EMAIL_CLICKED" : EMAIL_CLICKED,
                    "EMAIL_OPEN_RATE" : EMAIL_OPEN_RATE,
                    "EMAIL_CLICK_RATE" : EMAIL_CLICK_RATE,
                    "EMAIL_VERIFIED" : EMAIL_VERIFIED,
                    "EMAIL_BOUNCE_RATE" : EMAIL_BOUNCE_RATE,
                    "MESSAGE_REPLY_RATE" : MESSAGE_REPLY_RATE
                }
            }
            ]
        }
        r = requests.post(endpoint, json=data, headers=headers)
        print(r.text)
        
    print(r.status_code)

print("From airtable "+ str(r.status_code))
