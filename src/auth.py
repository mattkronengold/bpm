import sys
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