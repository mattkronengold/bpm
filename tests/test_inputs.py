#!/usr/bin/env python3

import unittest
from mock import patch
from src.inputs import get_length, get_genre, get_speed

class InputTestCase(unittest.TestCase):
    def length_test(self, given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer):
            length = get_length()
            self.assertEqual(length, expected_out)

    def test_length_10(self):
        self.length_test(10, 10)

    def genre_test(self, given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer):
            genre = get_genre()
            self.assertEqual(genre, expected_out)

    def test_genre_country(self):
        #input 6 is country
        self.genre_test(6, 6)

    def speed_test(self, given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer):
            speed = get_speed("start")
            self.assertEqual(speed, expected_out)

    def test_speed_150(self):
        self.speed_test(150, 150)
