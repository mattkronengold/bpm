import sys
import sqlite3

conn = sqlite3.connect("C:\\sqlite\bpm.db")
c = conn.cursor()

def logout():
    # get current user
    username = c.execute('SELECT username FROM User U JOIN Credentials C ON U.id = C.user_id;') # join on id
    user_id = c.execute('SELECT user_id FROM User U JOIN Credentials C ON U.id = C.user_id;') # get user_id of join
    username = username.fetchone()[0]
    user_id = user_id.fetchone()[0]
    print(username)
    print(user_id)

    # listen for logout
    if (input() == 'logout'):
        c.execute('DELETE FROM Credentials C WHERE C.user_id = ?;', (user_id,))
        conn.commit()
        # delete access_token and refresh_token from database
        # terminate program

logout()
