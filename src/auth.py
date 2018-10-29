import pickle
import requests
import sys
import time
import webbrowser

CLIENT_ID = '482102fb45cb45fdb465ef73801f4665'
CLIENT_SECRET = 'dc7269e0e5a84e71b9b27f857055b41f'
REDIRECT_URI = 'https://localhost/'
SCOPES = 'user-library-modify user-read-playback-state user-read-currently-playing user-modify-playback-state user-read-recently-played'

def authenticate():
	auth_req = "https://accounts.spotify.com/authorize" + \
	"?redirect_uri=" + REDIRECT_URI + \
	"&scope=" + SCOPES + \
	"&client_id=" + CLIENT_ID + \
	"&response_type=code" 
	auth_req.replace(":", "%3A").replace("/", "%2F").replace(" ", "+")
	webbrowser.open(auth_req)
	#finish login process

def get_code():
    print("Please copy and paste your validation code from the browser: ")
    auth_code = input()
    finish_auth(auth_code)

def finish_auth(auth_code):
    # application requests access tokens and refresh tokens
    resp = requests.post("https://accounts.spotify.com/api/token",
                         data={"grant_type": "authorization_code",
                               "redirect_uri": REDIRECT_URI,
                               "code": auth_code},
                         auth=(CLIENT_ID, CLIENT_SECRET))
    resp.raise_for_status()

    # pickle tokens so user does not have to re-authenticate
    resp_json = resp.json()
    pickle_data = {
        "access_token": resp_json["access_token"],
        "refresh_token": resp_json["refresh_token"],
        "expires_in": resp_json["expires_in"],
        "last_refreshed": time.time(),
    }

    # DO NOT DUMP TO PICKLE
    with open("token.pk", "wb") as pickle_file:
        pickle.dump(pickle_data, pickle_file)

    # sqlalchemy.whatever.exec('INSERT INTO user_auth (access_token, refresh_token, expires_in, last_refreshed) VALUES (%s, %s, %s, %s)', access_token, refresh_token, expires_in, last_refreshed)

authenticate() 
get_code()
