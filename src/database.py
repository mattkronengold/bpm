'''

@author: katiepfleger

'''
from __future__ import print_function
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    '''Creates a new db.'''
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        conn.close()

def create_user(db_file, print_err=True):
    ''' Creates a User table. '''
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE User
            (id integer PRIMARY KEY, username text UNIQUE)''')
    except Error as e:
        if print_err:
            print(e)
        else:
            pass
    finally:
        conn.close()

def create_credentials(db_file, print_err=True):
    ''' Creates a Credentials table. '''
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE Credentials (user_id integer PRIMARY KEY, \
        access_token text, refresh_token text, expires_at integer, last_refreshed \
        TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (user_id) REFERENCES User (id))''')
    except Error as e:
        if print_err:
            print(e)
        else:
            pass
    finally:
        conn.close()

def create_playlist(db_file, print_err=True):
    ''' Creates a Playlist table. '''
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE Playlist (tid text PRIMARY KEY, \
        name text, duration integer, bpm integer)''')
    except Error as e:
        if print_err:
            print(e)
        else:
            pass
    finally:
        conn.close()

def create_dislikes(db_file, print_err=True):
    ''' Creates a Playlist table. '''
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE Dislikes (tid text PRIMARY KEY)''')
    except Error as e:
        if print_err:
            print(e)
        else:
            pass
    finally:
        conn.close()

def verify_tables(db_file):
    '''Attempts to create all tables if they don't exist'''

    create_user(db_file, False)
    create_credentials(db_file, False)
    create_playlist(db_file, False)
    create_dislikes(db_file, False)

def insert_dislike(db_file, tid):
    '''Insert a song into the dislikes table'''

    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute('INSERT INTO Dislikes(tid) VALUES (?);', (tid,))
        conn.commit()

    except Error:
        pass

    finally:
        conn.close()

def is_disliked(db_file, tid):
    '''Check if a song is disliked'''

    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        tid = c.execute("SELECT * FROM Dislikes WHERE tid='%s'" \
            % tid).fetchone()
        return tid is not None
    except Error as e:
        print(e)
        return False
    finally:
        conn.close()

def remove_dislikes(db_file):
    ''' Remove all disliked songs '''

    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute('DELETE FROM Dislikes')
        conn.commit()
    except Error as e:
        print(e)
    finally:
        conn.close()
