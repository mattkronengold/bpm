'''

@author: torlofskii, alanaanderson

'''
from __future__ import print_function
import spotipy
import webbrowser

def create_playlist(token, tracks):
    """Creates playlist from user information and generated tracks"""
    spotify = spotipy.Spotify(auth=token)
    user = spotify.current_user()
    user_id = user["id"]

    final_song_list = []
    for track in tracks:
        final_song_list.append(track["tid"])

    name = input('Enter a name for your new playlist:\n')
    print()

    playlist = spotify.user_playlist_create(user_id, name)
    playlist_id = playlist['id']

    for song in final_song_list:
        spotify.user_playlist_add_tracks(user_id, playlist_id=playlist_id, tracks=[song])
    print("Would you like to open Spotify now?")
    print('0:\tYes')
    print('1:\tNo')
    open_spotify = input()
    print()
    if open_spotify == '0':
        webbrowser.open('http://open.spotify.com/playlist/'+ playlist_id)
    print('Your playlist has been saved to Spotify!')
