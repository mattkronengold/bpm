'''

@author: torlofski, mattkronengold

'''
import sqlite3
from sqlite3 import Error
import os.path
from src.database import create_connection, verify_tables, \
insert_dislike, is_disliked, remove_dislikes


def test_databases():
    '''Test the database'''

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
        assert playlist_table_exists

        dislikes_table_exists = c.execute("SELECT count(*) from \
            sqlite_master WHERE type='table' AND name='Dislikes'").fetchone()
        assert dislikes_table_exists

    except Error as e:
        print(e)
    finally:
        conn.close()
        os.remove(db_file)

def test_dislikes():
    ''' Test dislike feature'''

    db_file = "bpm_t.db"
    verify_tables(db_file)

    assert not is_disliked(db_file, '100')

    insert_dislike(db_file, '101')
    assert is_disliked(db_file, '101')

    insert_dislike(db_file, '103')
    insert_dislike(db_file, '104')
    assert is_disliked(db_file, '101')
    assert is_disliked(db_file, '103')
    assert is_disliked(db_file, '104')

    remove_dislikes(db_file)

    for tid in ['100', '101', '102', '103', '104']:
        assert not is_disliked(db_file, tid)

    os.remove(db_file)
