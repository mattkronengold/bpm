import sys
import sqlite3

conn = sqlite3.connect("bpm.db")
c = conn.cursor()

def logout():
    try:
        # get current user
        user_id = c.execute('SELECT C.user_id FROM Credentials C').fetchone()[0] 
        # remove from credentials table
        c.execute('DELETE FROM Credentials WHERE user_id = ?;', (user_id,))
        conn.commit()
        # exit program
        sys.exit(0)
    except:
        print('There are no users logged into the system')


logout()
