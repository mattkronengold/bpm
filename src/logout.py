'''
    @author: alanaanderson
'''
from __future__ import print_function
import sys
import sqlite3
from playlist_cache import remove_playlist_cache
from database import remove_dislikes


def check_input(user_input):
    '''
        Checks if a user has entered the logout keyword
    '''
    if user_input == "logout":
        logout('bpm.db')

def logout(db_file):
    '''
        Removes user from Credentials table to log out that user.
    '''
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()

        # get current user
        user_id = c.execute('SELECT C.user_id FROM Credentials C').fetchone()
        if user_id:
            user_id = user_id[0]
        else:
            raise ValueError
        # remove from credentials table
        c.execute('DELETE FROM Credentials WHERE user_id = ?;', (user_id,))
        conn.commit()
        remove_playlist_cache(db_file)
        remove_dislikes(db_file)
        # exit program
        sys.exit(0)
    except ValueError:
        print('There are no users logged into the system')
