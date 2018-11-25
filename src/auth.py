'''

@author: katiepfleger

'''
from __future__ import print_function
import sqlite3
import webbrowser
from spotipy import oauth2
from logout import check_input


CONN = sqlite3.connect("bpm.db")
C = CONN.cursor()

CLIENT_ID = '482102fb45cb45fdb465ef73801f4665'
CLIENT_SECRET = 'dc7269e0e5a84e71b9b27f857055b41f'
REDIRECT_URI = 'https://localhost/'
SCOPES = 'user-library-modify user-library-read user-read-playback-state \
user-read-currently-playing user-modify-playback-state user-read-recently-played \
playlist-read-private playlist-modify-public playlist-modify-private \
playlist-read-collaborative'

def welcome():
    '''
        Performs the user authentication and login flow
    '''
    login_result = C.execute('SELECT COUNT(*) FROM Credentials').fetchone()[0]
    if login_result == 1:
        print('Welcome back to BPM!\n')
        return True
    else:
        print('\nWelcome to BPM!')
        print('\nDo you have a BPM account?')
        print('0:\tYes')
        print('1:\tNo')
        has_account = input()
        check_input(has_account)
        if has_account == '0':
            user_id = get_username()
            if user_id:

                auth = oauth2.SpotifyOAuth(CLIENT_ID, CLIENT_SECRET,
                                           REDIRECT_URI, scope=SCOPES)
                authenticate(auth)
                get_code(auth, user_id)
                CONN.close()
                return True
            else:
                return False
        else:
            print('\nDo you have a Spotify account?')
            print('0:\tYes')
            print('1:\tNo')
            has_spotify = input()
            check_input(has_spotify)
            if has_spotify == '0':

                auth = oauth2.SpotifyOAuth(CLIENT_ID, CLIENT_SECRET,
                                           REDIRECT_URI, scope=SCOPES)
                user_id = create_username()
                authenticate(auth)
                get_code(auth, user_id)
                CONN.close()
                return True
            else:
                print('\nPlease sign up for a Spotify account and return.\n')
                return False

def get_username():
    '''
        Checks for existing BPM users.
    '''
    username = input('\nEnter your BPM username: ')
    check_input(username)
    try:
        user_id = C.execute("SELECT U.id FROM User U WHERE U.username='%s'" \
            % username).fetchone()
        if user_id:
            return user_id[0]
        else:
            print('\nThere are no users with that username.')
            return create_username()
    except ValueError:
        print('\nThere are no users with that username. \
            Would you like to try again or create a new account?')
        print('0:\tTry Again')
        print('1:\tCreate New Account')
        if input() == '0':
            return get_username()
        else:
            print('\nDo you have a Spotify account?')
            print('0:\tYes')
            print('1:\tNo')
            has_spotify = input()
            check_input(has_spotify)
            if has_spotify == '0':
                return create_username()
            else:
                print('Please sign up for a Spotify account and return.\n')
                return False

def create_username():
    '''
        Creates new BPM user.
    '''
    username = input('\nPlease enter a username for your new BPM account:\n')
    check_input(username)
    try:
        C.execute('INSERT INTO User(username) VALUES (?);', (username,))
        CONN.commit()
        user_id = C.execute('SELECT U.id FROM User U WHERE U.username=?;', \
            (username,)).fetchone()[0]
        return user_id
    except ValueError:
        print('\nThat username is already taken. Please enter a different username.\n')
        return create_username()

def authenticate(auth):
    '''
        Authenticates current user with the BPM app in Spotify.
    '''
    webbrowser.open(auth.get_authorize_url())

def get_code(auth, user_id):
    '''
        Prompts user to enter validation code that they are redirected to.
    '''
    print("\nPlease copy and paste your validation code from the browser: ")
    auth_code = input()
    check_input(auth_code)
    finish_auth(auth, user_id, auth_code)

def finish_auth(auth, user_id, auth_code):
    '''
        Adds user authentication tokens to Credentials.
    '''
    response = auth.get_access_token(auth_code)
    access_token = response["access_token"]
    refresh_token = response["refresh_token"]
    expires_in = response["expires_in"]

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
