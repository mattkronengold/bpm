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

def create_user(db_file):
    ''' Creates a User table. '''
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE User
            (id integer PRIMARY KEY, username text UNIQUE)''')
    except Error as e:
        print(e)
    finally:
        conn.close()

def create_credentials(db_file):
    ''' Creates a Credentials table. '''
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE Credentials (user_id integer PRIMARY KEY, \
        access_token text, refresh_token text, expires_in text, last_refreshed \
        TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (user_id) REFERENCES User (id))''')
    except Error as e:
        print(e)
    finally:
        conn.close()
