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

    final_song_list = []
    for track in tracks:
        final_song_list.append(track["tid"])

    name = input('Enter a name for your new playlist!\n')

    playlist = spotify.user_playlist_create(user_id, name)
    playlist_id = playlist['id']

    for song in final_song_list:
        spotify.user_playlist_add_tracks(user_id, playlist_id=playlist_id, tracks=[song])
    print("Added tracks to playlist!")
