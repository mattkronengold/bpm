'''

@author: torlofski

'''

import unittest
import sqlite3
import os.path
from src.database import create_connection, create_playlist
from playlist_cache import cache_playlist, get_playlist_cache, \
    remove_playlist_cache

class CacheTestCase(unittest.TestCase):
    """Tests cache_playlist"""

    def setUp(self):
        create_connection('bpm_test.db')
        create_playlist('bpm_test.db', False)

    def test_caching_playlist(self):
        """Tests that playlist caching is successful"""

        test_playlist = [{"tid": "100", "name": "testsong1", "duration": 10, "bpm":10}, \
        {"tid": "200", "name": "testsong2", "duration": 10, "bpm":10}]

        cache_playlist(test_playlist, 'bpm_test.db')
        CONN = sqlite3.connect('bpm_test.db')
        C = CONN.cursor()
        playlist = C.execute('SELECT * FROM Playlist').fetchall()
        CONN.commit()
        CONN.close()
        playlist_list = []
        for p in playlist:
            playlist_list.append({"tid": p[0], "name": p[1], "duration": p[2], "bpm": p[3]})

        self.assertEqual(test_playlist, playlist_list)

    def tearDown(self):
        os.remove('bpm_test.db')

class GetCacheTestCase(unittest.TestCase):
    """Tests get_playlist_cache"""

    def setUp(self):
        test_playlist = [{"tid": "100", "name": "testsong1", "duration": 10, "bpm":10}, \
        {"tid": "200", "name": "testsong2", "duration": 10, "bpm":10}]

        create_connection('bpm_test.db')
        create_playlist('bpm_test.db', False)

        CONN = sqlite3.connect('bpm_test.db')
        C = CONN.cursor()
        for p in test_playlist:
            C.execute('INSERT INTO Playlist(tid, name, duration, bpm) VALUES(?, ?, ?, ?);', \
                (p["tid"], p["name"], p["duration"], p["bpm"]))
        CONN.commit()
        CONN.close()

    def test_get_cache(self):
        """Tests that get_cache correctly reads input from database"""

        test_playlist = [{"tid": "100", "name": "testsong1", "duration": 10, "bpm":10}, \
        {"tid": "200", "name": "testsong2", "duration": 10, "bpm":10}]

        playlist_gotten = get_playlist_cache('bpm_test.db')

        self.assertEqual(test_playlist, playlist_gotten)

    def tearDown(self):
        os.remove('bpm_test.db')

class RemoveCacheTestCase(unittest.TestCase):
    """Tests remove_playlist_cache"""

    def setUp(self):
        test_playlist = [{"tid": "100", "name": "testsong1", "duration": 10, "bpm":10}, \
        {"tid": "200", "name": "testsong2", "duration": 10, "bpm":10}]

        create_connection('bpm_test.db')
        create_playlist('bpm_test.db', False)

        CONN = sqlite3.connect('bpm_test.db')
        C = CONN.cursor()
        for p in test_playlist:
            C.execute('INSERT INTO Playlist(tid, name, duration, bpm) VALUES(?, ?, ?, ?);', \
                (p["tid"], p["name"], p["duration"], p["bpm"]))
        CONN.commit()
        CONN.close()

    def test_remove_cache(self):
        """Tests that the cache is there before and gone after"""

        CONN = sqlite3.connect('bpm_test.db')
        C = CONN.cursor()
        cache_exists = C.execute('SELECT *  FROM Playlist').fetchone()
        self.assertIsNotNone(cache_exists)
        CONN.commit()
        CONN.close()
        remove_playlist_cache('bpm_test.db')

        CONN = sqlite3.connect('bpm_test.db')
        C = CONN.cursor()
        cache_exists = C.execute('SELECT * FROM Playlist').fetchone()
        self.assertIsNone(cache_exists)
        CONN.commit()
        CONN.close()

    def tearDown(self):
        os.remove('bpm_test.db')
