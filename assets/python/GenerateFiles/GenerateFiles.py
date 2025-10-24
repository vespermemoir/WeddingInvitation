from google.oauth2 import service_account
from googleapiclient.discovery import build

import uuid, os
import json

SERVICE_ACCOUNT_FILE = 'credentials-3.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SHEET_ID = '14oZb1LvIVZohazwCBo4wiRcT7e0nJuSUsdcgM7D55IM'
RANGE = 'ListOfGuests!A1:E100'

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

result = sheet.values().get(spreadsheetId=SHEET_ID, range=RANGE).execute()
InvitationData = result.get('values', [])

headers = InvitationData[0]
rows = InvitationData[1:]
dict_list = [dict(zip(headers, row + [''] * (len(headers) - len(row)))) for row in rows]

for guest in dict_list:
    if not guest["GuestID"]:
        guest["GuestID"] = str(uuid.uuid4())

updated_data = [headers] + [[guest[h] for h in headers] for guest in dict_list]

sheet.values().update(
    spreadsheetId=SHEET_ID,
    range=f'ListOfGuests!A1',
    valueInputOption='RAW',
    body={'values': updated_data}
).execute()