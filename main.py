import os
import requests

from dotenv import load_dotenv
load_dotenv()

import accountid_name

print("Started accountid name migration.")
accountid_name()
print("Finished accountid name migration.")

r = requests.post(endpoint, json=data, headers=headers)
print(r.status_code)