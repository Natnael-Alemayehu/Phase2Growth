import os
import requests


from dotenv import load_dotenv
load_dotenv()

print("Writing all the account ID's")
import write_all_account
print("Writing all the account ID's that are active")
import write_to_accountid_active
print("Writing all the account ID's that are expired")
import write_to_accountid_expired
print("Writing account Id's is complete")
# import accountid_name
# import leads
# import tags
# import clients
# import teams
# import campaign


# r = requests.post(endpoint, json=data, headers=headers)
# print(r.status_code)
