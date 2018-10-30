'''

@author: torlofski

'''
from __future__ import print_function
import spotipy

def create_playlist(token, tracks):
    """Creates playlist from user information and generated tracks"""
    spotify = spotipy.Spotify(auth=token)
    user = spotify.current_user()
    user_id = user["id"]
    print(user_id)

    name = input('Enter a name for your new playlist!\n')
    print()

    playlist = spotify.user_playlist_create(user_id, name)
    print("Playlist generated with name: " + name)

    spotify.user_playlist_add_tracks(user_id, playlist, tracks)
    print("Added tracks to playlist!")
