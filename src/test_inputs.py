#!/usr/bin/env python3
'''

@author: torlofski

'''

import unittest
from mock import patch
from src.inputs import get_length, get_genre, get_speed

class InputTestCase(unittest.TestCase):
    """Input tests"""

    def length_test(self, given_answer, expected_out):
        """Test get_length"""
        with patch('builtins.input', return_value=given_answer):
            length = get_length()
            self.assertEqual(length, expected_out)

    def test_length_10(self):
        """Call length test"""
        self.length_test(10, 10)

    def genre_test(self, given_answer, expected_out):
        """Test get_genre"""
        with patch('builtins.input', return_value=given_answer):
            genre = get_genre()
            self.assertEqual(genre, expected_out)

    def test_genre_country(self):
        """Call genre test"""
        #input 6 is country
        self.genre_test(6, 6)

    def speed_test(self, given_answer, expected_out):
        """Test get_speed"""
        with patch('builtins.input', return_value=given_answer):
            speed = get_speed("start")
            self.assertEqual(speed, expected_out)

    def test_speed_150(self):
        """Call speed test"""
        self.speed_test(150, 150)
