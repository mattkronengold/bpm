'''

@author: torlofski

'''
from __future__ import print_function
import spotipy

def create_playlist(token, user_id, tracks):
    """Creates playlist from user information and generated tracks"""
    spotify = spotipy.Spotify(auth=token)

    name = input('Enter a name for your new playlist!')

    playlist = spotify.user_playlist_create(user_id, name, 'Generated by BPM')
    print("Playlist generated with name: " + name)

    spotify.user_playlist_add_tracks(user_id, playlist, tracks)
    print("Added tracks to playlist!")