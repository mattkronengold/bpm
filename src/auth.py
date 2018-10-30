'''

@author: katiepfleger

'''
from __future__ import print_function
import sqlite3
import webbrowser
import requests


CONN = sqlite3.connect("bpm.db")
C = CONN.cursor()

CLIENT_ID = '482102fb45cb45fdb465ef73801f4665'
CLIENT_SECRET = 'dc7269e0e5a84e71b9b27f857055b41f'
REDIRECT_URI = 'https://localhost/'
SCOPES = 'user-library-modify user-library-read user-read-playback-state \
user-read-currently-playing user-modify-playback-state user-read-recently-played'

def welcome():
    '''
        Performs the user authentication and login flow
    '''
    login_result = C.execute('SELECT COUNT(*) FROM Credentials').fetchone()[0]
    if login_result == 1:
        print('Welcome back to BPM!')
        return True
    else:
        print('Welcome to BPM!')
        print('Do you have a BPM account?')
        print('0:\tYes')
        print('1:\tNo')
        has_account = input()

        if has_account == '0':
            user_id = get_username()
            if user_id:
                authenticate()
                get_code(user_id)
                CONN.close()
                return True
            else:
                return False
        else:
            print('Do you have a Spotify account?')
            print('0:\tYes')
            print('1:\tNo')
            has_spotify = input()
            if has_spotify == '0':
                user_id = create_username()
                authenticate()
                get_code(user_id)
                CONN.close()
                return True
            else:
                print('Please sign up for a Spotify account and return.\n')
                return False

def get_username():
    '''
        Checks for existing BPM users.
    '''
    username = input('Enter your BPM username: ')
    try:
        user_id = C.execute("SELECT U.id FROM User U WHERE U.username='%s'" \
            % username).fetchone()[0]
        return user_id
    except ValueError:
        print('There are no users with that username. \
            Would you like to try again or create a new account?')
        print('0:\tTry Again')
        print('1:\tCreate New Account')
        if input() == '0':
            return get_username()
        else:
            print('Do you have a Spotify account?')
            print('0:\tYes')
            print('1:\tNo')
            has_spotify = input()
            if has_spotify == '0':
                return create_username()
            else:
                print('Please sign up for a Spotify account and return.\n')
                return False

def create_username():
    '''
        Creates new BPM user.
    '''
    username = input('Please enter a username for your new BPM account\n')
    try:
        C.execute('INSERT INTO User(username) VALUES (?);', (username,))
        CONN.commit()
        user_id = C.execute('SELECT U.id FROM User U WHERE U.username=?;', \
            (username,)).fetchone()[0]
        return user_id
    except ValueError:
        print('That username is already taken. Please enter a different username.\n')
        return create_username()

def authenticate():
    '''
        Authenticates current user with the BPM app in Spotify.
    '''
    auth_req = "https://accounts.spotify.com/authorize" + \
	"?redirect_uri=" + REDIRECT_URI + \
	"&scope=" + SCOPES + \
	"&client_id=" + CLIENT_ID + \
	"&response_type=code"
    auth_req.replace(":", "%3A").replace("/", "%2F").replace(" ", "+")
    webbrowser.open(auth_req)

def get_code(user_id):
    '''
        Prompts user to enter validation code that they are redirected to.
    '''
    print("Please copy and paste your validation code from the browser: ")
    auth_code = input()
    finish_auth(user_id, auth_code)

def finish_auth(user_id, auth_code):
    '''
        Adds user authentication tokens to Credentials.
    '''
    resp = requests.post("https://accounts.spotify.com/api/token",
                         data={"grant_type": "authorization_code",
                               "redirect_uri": REDIRECT_URI,
                               "code": auth_code},
                         auth=(CLIENT_ID, CLIENT_SECRET))
    resp.raise_for_status()
    resp_json = resp.json()

    access_token = resp_json["access_token"]
    refresh_token = resp_json["refresh_token"]
    expires_in = resp_json["expires_in"]

    C.execute('INSERT INTO Credentials(user_id, access_token, refresh_token, expires_in) \
        VALUES (?, ?, ?, ?);', (user_id, access_token, refresh_token, expires_in))
    CONN.commit()

def get_current_user_token():
    '''
        Retrieves current user's access token.
    '''
    local_conn = sqlite3.connect("bpm.db")
    c = local_conn.cursor()
    access_token = c.execute('SELECT C.access_token FROM Credentials C').fetchone()[0]
    local_conn.close()
    return access_token
