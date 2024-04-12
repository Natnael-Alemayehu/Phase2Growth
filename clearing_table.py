import os
import requests
from timestamp_convert import convert_timestamp_to_datetime
from timestamp_convert import convert_datetime_to_timestamp
from return_fromtxt import read_all_account_ids
from dotenv import load_dotenv
load_dotenv()

# Replace with your actual values
AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME = 'iterative_clear_test'

# Endpoint for retrieving records
endpoint = f'https://api.airtable.com/v0/apphrxDtb300tgxfL/{AIRTABLE_TABLE_NAME}'

# Headers with API key
headers = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}",
    "Content-Type" : "application/json"
}

# Get all records
response = requests.get(endpoint, headers=headers)
print(response)
# records = response.json().get("records", [])
# print(response)
# # Delete each record
# for record in records:
#     record_id = record.get("id")
#     print("Hello")
#     print(record_id)
#     delete_url = f"{endpoint}/{record_id}"
#     requests.delete(delete_url, headers=headers)
#     print(f"Deleted record with ID: {record_id}")

# print("All records deleted successfully!")



# Old file

