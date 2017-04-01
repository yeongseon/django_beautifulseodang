import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('Beautifulseodang-c0a5cc61a537.json', scope)
client = gspread.authorize(creds)

sheet = client.open("test").sheet1


list_of_hashes = sheet.get_all_records()
print (list_of_hashes)