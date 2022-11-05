from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# defining the scope of the application
scope_app =['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'] 
SAMPLE_SPREADSHEET_ID="1UTZVoUZcLV9AN2YxdzNcXRxIj1q7vFdh3slMd7ns354"
#credentials to the account
cred = service_account.Credentials.from_service_account_file('/home/zec/Desktop/smart_home/smart_homes.json', scopes=scope_app) 
service = build('sheets', 'v4',credentials=cred)
sheet = service.spreadsheets()

# NOTE: Clears only entered values, but preserves cell format.
# requests = []
# requests.append({
#         "updateCells": {
#             "range": {
#                 "sheetId": sheets[4]['1653535723']
#             },
#             'fields': 'userEnteredValue'
#         }
# })

# body = {
#     'requests': requests
# }

with open('mexico_company_list.csv', 'r') as file_obj:
    content = file_obj.read()
    for i in content:
        k=[i]
        sheet.values().append(spreadsheetId = SAMPLE_SPREADSHEET_ID, range= 'USA!A2', valueInputOption = "USER_ENTERED", body = { "majorDimension": "ROWS",'values':k}).execute()