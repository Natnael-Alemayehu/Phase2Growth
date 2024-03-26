import os
from account_expire_check import expired_accountid



os.makedirs("account", exist_ok=True)

# Get the list from your function
data_to_write = expired_accountid()

# Open the file in write mode
with open(os.path.join("account", "accountid_expired.txt"), "w") as f:
    # Write each item in the list to the file, separated by a newline
    for item in data_to_write:
        f.write(f"{item}\n")

print("List successfully written to account.txt!")