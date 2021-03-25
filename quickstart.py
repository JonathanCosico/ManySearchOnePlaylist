from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1kzdECh1SB48M5cRr51EH-mkrJIGgoUfwnmRtB4U4cus'
SAMPLE_RANGE_NAME = 'Songs!A2:C' # 'Class Data!A2:E' 

# verify google credentials
# return service object
def verifyID():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    return service

def getSongArtistList(values):
    songArtistList = []
    if not values:
        print('No data found.')
        return songArtistList
    else:
        print('Song, Artist:')
        for row in values:
            # Print columns A and C, which correspond to indices 0 and 2.
            if row[0] != "" and row[1] != "":
                print(f"{row[0]} - {row[1]}")
                # print('%s - %s' % (row[0], row[1]))
                # songArtistList.append("%s %s" % (row[0], row[1]))
                songArtistList.append(f"{row[0]} {row[1]}")
    return songArtistList

    print(len(getSongArtistList()))



def main():
    service = verifyID()

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', []) # gets a list of requested values | single row: [row[0], row[1], ...]
    getSongArtistList(values)
    



    # value_range_body = {
    # # TODO: Add desired entries to the request body. All existing entries
    # # will be replaced.

    # }

    # request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body)
    # response = request.execute()

    # # TODO: Change code below to process the `response` dict:
    # pprint(response)



if __name__ == '__main__':
    main()