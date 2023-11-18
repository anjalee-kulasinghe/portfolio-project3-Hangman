import gspread
from google.oauth2.service_account import Credentials
import random
import hangman_stages

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('score_board')

'''
score = SHEET.worksheet('score')
data = score.get_all_values()
print(data)
'''

def get_username():
    '''
    to get the username from the user
    '''
    data_username = input('Please enter your username: ')
    print(f"Username given is {data_username}")

get_username()
