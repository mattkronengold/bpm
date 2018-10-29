import sys
import sqlite3

conn = sqlite3.connect("C:\\sqlite\bpm.db")
c = conn.cursor()

def logout():
    # get current user
    user_id = c.execute('SELECT C.user_id FROM Credentials C').fetchone()[0] # get user_id of join
    print(user_id)

    # listen for logout
    if (input() == 'logout'):
        c.execute('DELETE FROM Credentials WHERE user_id = ?;', (user_id,))
        conn.commit()

logout()
