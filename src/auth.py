import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials


try:
    spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

except spotipy.oauth2.SpotifyOauthError:
    print('Did not find Spotify credentials.')
    print('Please visit https://github.com/bjarneo/pytify#credentials for more information.')
    sys.exit(1) 


