#!/usr/bin/env python3
'''

@author: torlofski

'''

import unittest
import sqlite3
import os
from mock import patch
from logout import logout, check_input
from database import create_connection, create_user, create_credentials

class CheckInputTestCase(unittest.TestCase):
    """check_input function tests"""

    def test_logout_called(self):
        """Test that logout() is called when proper"""
        with patch('logout.logout', return_value='test') as mock:
            check_input('logout')
        self.assertTrue(mock.called)

    def test_logout_not_called(self):
        """Test that logout() is not called when improper"""
        with patch('logout.logout', return_value='test') as mock:
            check_input('logou')
            check_input('ogout')
            check_input('log out')
            check_input('some other string')
            check_input(67)
        self.assertFalse(mock.called)

class LogoutTestCase(unittest.TestCase):
    """logout function tests"""

    def setUp(self):
        create_connection('bpm_test.db')
        create_user('bpm_test.db')
        create_credentials('bpm_test.db')

        conn = sqlite3.connect('bpm_test.db')
        c = conn.cursor()
        c.execute('INSERT INTO User(id, username) VALUES (123456, "test_user")')
        c.execute('INSERT INTO Credentials (user_id, access_token, \
            refresh_token, expires_at) VALUES (123456, "test_token", \
            "test_token", 21)')
        conn.close()

    def tearDown(self):
        os.remove('bpm_test.db')

    def test_proper_logout(self):
        """Tests that logout is doing what it should under normal input"""
        conn = sqlite3.connect('bpm_test.db')
        c = conn.cursor()

        #these 2 lines are to make sure that the setup function ran correctly
        credentials_table_exists = c.execute("SELECT count(*) from \
            Credentials").fetchone()
        self.assertIsNotNone(credentials_table_exists)

        logout('bpm_test.db')

        user_id2 = c.execute('SELECT C.user_id FROM Credentials C').fetchone()
        self.assertIsNone(user_id2)
        conn.close()
