'''

@author: katiepfleger

'''
from __future__ import print_function
import sqlite3

def cache_playlist(playlist, db_file):
    CONN = sqlite3.connect(db_file)
    C = CONN.cursor()
    for p in playlist:
        C.execute('INSERT INTO Playlist(tid, name, duration, bpm) VALUES(?, ?, ?, ?);', \
            (p["tid"], p["name"], p["duration"], p["bpm"]))
    CONN.commit()
    CONN.close()

def get_playlist_cache(db_file):
    try:
        CONN = sqlite3.connect(db_file)
        C = CONN.cursor()
        playlist = C.execute('SELECT * FROM Playlist').fetchall()
        CONN.commit()
        CONN.close()
        playlist_list = []
        for p in playlist:
            playlist_list.append({"tid": p[0], "name": p[1], "duration": p[2], "bpm": p[3]})
        return playlist_list
    except:
        return 0

def remove_playlist_cache(db_file):
    CONN = sqlite3.connect(db_file)
    C = CONN.cursor()
    C.execute('DELETE FROM Playlist')
    CONN.commit()
    CONN.close()

def check_cache(print_playlist, db_file):
    if(get_playlist_cache(db_file)):
        print("The following playlist did not save to Spotify in your last session: ")
        print_playlist(get_playlist_cache(db_file))
        print("Would you like to save it now?")
        print("0:\tYes")
        print("1:\tNo")
        resp = input()
        print()
        if resp == '0':
            return 1
        elif resp == '1':
            remove_playlist_cache(db_file)
            print("Let's create another playlist!")
    return 0
