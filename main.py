import os
import requests


from dotenv import load_dotenv
load_dotenv()

import write_all_account
import accountid_name
import campaign
import tags
import teams
import leads
import clients


# # listing out the accountids in the API table populate
# print("Started wrotting accountid's to txt loading .......")
# write_all_account()
# print("Finished writing accountid's to txt loading .......")

# name-accountid table populate
print("Started accountid name loading .......")
accountid_name()
print("Finished accountid name loading .......")

# # campaign table populate
# print("Started campaign data loading ........")
# campaign()
# print("Finished campaign data loading ........")

# # tags table populate
# print("Started tags data loading ........")
# tags()
# print("Finished tags data loading ........")

# # teams table populate
# print("Started teams data loading ........")
# teams()
# print("Finished teams data loading ........")

# # leads table populate
# print("Started leads data loading ........")
# teams()
# print("Finished leads data loading ........")

# # clients table populate
# print("Started clients data loading ........")
# teams()
# print("Finished clients data loading ........")

