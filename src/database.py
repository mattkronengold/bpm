import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        conn.close()

def create_user(db_file):
	try:
		conn = sqlite3.connect(db_file)
		c=conn.cursor()
		c.execute('''CREATE TABLE User
	             (id integer PRIMARY KEY, username text UNIQUE)''')
	except Error as e:
		print(e)
	finally:
		conn.close()

def create_credentials(db_file):
	try:
		conn = sqlite3.connect(db_file)
		c=conn.cursor()
		c.execute('''CREATE TABLE Credentials
	             (user_id integer PRIMARY KEY, access_token text, refresh_token text, expires_in text, \
	              last_refreshed TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (user_id) REFERENCES User (id))''')
	except Error as e:
		print(e)
	finally:
		conn.close()
	

if __name__ == '__main__':
	conn = sqlite3.connect("C:\\sqlite\bpm.db")
	# c=conn.cursor()
	# c.execute('INSERT INTO User (username) VALUES (?);', ("katie",))
	# rows = c.fetchall()
	# for row in rows:
		# print(row)
	# conn.close()