'''

@author: torlofski

'''
import sqlite3
from sqlite3 import Error
import os.path
from src.database import create_connection, verify_tables


def test_databases():
    """Test the database"""

    db_file = "bpm_t.db"

    try:
        create_connection(db_file)
        assert os.path.isfile(db_file)

        verify_tables(db_file)

        conn = sqlite3.connect(db_file)
        c = conn.cursor()

        user_table_exists = c.execute("SELECT count(*) from \
            sqlite_master WHERE type='table' AND name='User'").fetchone()
        assert user_table_exists

        creds_table_exists = c.execute("SELECT count(*) from \
            sqlite_master WHERE type='table' AND name='Credentials'").fetchone()
        assert creds_table_exists

        playlist_table_exists = c.execute("SELECT count(*) from \
            sqlite_master WHERE type='table' AND name='Playlist'").fetchone()
        assert creds_table_exists

        dislikes_table_exists = c.execute("SELECT count(*) from \
            sqlite_master WHERE type='table' AND name='Dislikes'").fetchone()
        assert dislikes_table_exists

    except Error as e:
        print(e)
    finally:
        conn.close()
        os.remove(db_file)
