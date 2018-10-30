'''

@author: torlofski

'''
import sqlite3
from sqlite3 import Error
import os.path
from src.database import create_connection, create_user, create_credentials


def test_databases():
    """Test the database"""

    db_file = "bpm_t.db"

    try:
        create_connection(db_file)
        assert os.path.isfile(db_file)

        create_user(db_file)
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        user_table_exists = c.execute("SELECT count(*) from \
            sqlite_master WHERE type='table' AND name='user'").fetchone()
        assert user_table_exists

        create_credentials(db_file)
        creds_table_exists = c.execute("SELECT count(*) from \
            sqlite_master WHERE type='table' AND name='credentials'").fetchone()
        assert creds_table_exists
    except Error as e:
        print(e)
    finally:
        conn.close()
