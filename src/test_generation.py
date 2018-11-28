'''

@author: mattkronengold

'''
import sqlite3
from sqlite3 import Error
import os.path
from src.database import create_connection, create_user, create_credentials
from auth import get_current_user_token
from generation import run_gen

DB_FILE = "bpm_gen_t.db"

def setup():
    ''' Configure the database for the test '''
    create_connection(DB_FILE)
    create_user(DB_FILE)
    create_credentials(DB_FILE)

def teardown():
    ''' Cleanup after the tests '''

    os.remove(DB_FILE)

def test_auth_gen():
    ''' Test authentication and generation '''

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    access_token = 'BQCsyoKsDETKXe0h3G_dxo_OEOK5k79qoGfQuW3taiSRN4JG10UkYjDuBXXRFqKL5akBlANzHcKxGPHITaQInQGSybaQ2DQW1TRlQIOtzBGwzr36iY5jo1UvdcqLk8Iae1SQDbIdy-QisHc6bZVGwxOExhejANaYkKYuHu2XfxhqZ8jLGiRIp3XNj0Trtkt0i9PsosqQ0f_AEiv9keAIctju_wZAc13lYykb7q-ksmegf4eFFaW6ywBfrFf4zmMjdXecgfVm'
    refresh_token = 'AQCr7hLK2vLBRX0YugAe9irbJVt_ysPZliCDUoXK0Uln4fJ77UevTsigVOPCi2-J-kJFX0ODiDTsptklfa4o-a0y5B1KC_Z5IXnKfMNXi53lUFcy3wyhVMIjPQqOzM4DHSYF8w'
    expires_at = '0' # Always refresh

    c.execute('INSERT INTO Credentials(user_id, access_token, refresh_token, expires_at) \
        VALUES (?, ?, ?, ?);', (1, access_token, refresh_token, expires_at))
    conn.commit()

    token = get_current_user_token(DB_FILE)
    assert access_token != token # Should have refreshed

    conn.close()

    inputs = {"genre": 0,
              "length": 20,
              "start_speed": 100,
              "end_speed": 200}

    generation = run_gen(token, inputs)
    library = generation["library"]
    playlist = generation["playlist"]

