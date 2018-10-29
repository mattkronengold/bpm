import sys
import sqlite3

conn = sqlite3.connect("C:\\sqlite\bpm.db")
c = conn.cursor()

def logout():
    # get current user
    username = c.execute('SELECT username FROM User U JOIN Credentials C ON U.id = C.user_id;')
    print(username[0])

    # listen for logout
    if (input() == 'logout'):
        c.execute('DELETE FROM User U WHERE U.username = ?;', (username,))
        conn.commit()
        # delete access_token and refresh_token from database
        # terminate program

logout()
