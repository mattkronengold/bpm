import sqlite3
import requests
import sys
import datetime
import webbrowser

conn = sqlite3.connect("C:\\sqlite\bpm.db")
c = conn.cursor()

CLIENT_ID = '482102fb45cb45fdb465ef73801f4665'
CLIENT_SECRET = 'dc7269e0e5a84e71b9b27f857055b41f'
REDIRECT_URI = 'https://localhost/'
SCOPES = 'user-library-modify user-read-playback-state user-read-currently-playing user-modify-playback-state user-read-recently-played'

def welcome():
    login_result = c.execute('SELECT COUNT(*) FROM Credentials').fetchone()[0]
    if login_result == 1:
        print('Welcome back to BPM!')
        return True
    else:
        print('Welcome to BPM!')
        print('Do you have a Spotify account?')
        print('0:\tyes')
        print('1:\tno')
        has_account = input()

        if (has_account == '0'):
            user_id = create_username()
            authenticate()
            get_code(user_id)
            conn.close()
            return True
        else:
            print('Please sign up for a Spotify account and return.\n')
            return False


def create_username():
    username = input('Please enter a username for your new BPM account\n')
    try:
        c.execute('INSERT INTO User(username) VALUES (?);', (username,))
        conn.commit()
        user_id = c.execute('SELECT U.id FROM User U WHERE U.username=?;', (username,))
        conn.commit()
        return user_id.fetchone()[0]
    except:
        print('That username is already taken. Please enter a different username.\n')
        create_username()

def authenticate():
	auth_req = "https://accounts.spotify.com/authorize" + \
	"?redirect_uri=" + REDIRECT_URI + \
	"&scope=" + SCOPES + \
	"&client_id=" + CLIENT_ID + \
	"&response_type=code"
	auth_req.replace(":", "%3A").replace("/", "%2F").replace(" ", "+")
	webbrowser.open(auth_req)

def get_code(user_id):
    print("Please copy and paste your validation code from the browser: ")
    auth_code = input()
    finish_auth(user_id, auth_code)

def finish_auth(user_id, auth_code):
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

    c.execute('INSERT INTO Credentials(user_id, access_token, refresh_token, expires_in) VALUES (?, ?, ?, ?);', (user_id, \
        access_token, refresh_token, expires_in))
    conn.commit()
