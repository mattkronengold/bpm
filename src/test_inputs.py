#!/usr/bin/env python3
'''

@author: torlofski

'''

import unittest
import io
from contextlib import redirect_stdout
from mock import patch
from src.inputs import get_length, get_genre, get_speed

class InputTestCase(unittest.TestCase):
    """Input tests"""

    def length_test(self, given_answer, expected_out):
        """Test get_length"""
        with patch('builtins.input', return_value=given_answer):
            length = get_length()
            self.assertEqual(length, expected_out)

    def test_length(self):
        """Call length test"""
        self.length_test(5, 5)
        self.length_test(6, 6)
        self.length_test(90, 90)
        self.length_test(89, 89)
        self.length_test(45, 45)

    def length_improper_input_test(self, input_stream):
        """Test handling incorrect input in get_length"""
        with patch('builtins.input', side_effect=input_stream):
            f = io.StringIO()
            with redirect_stdout(f):
                get_length()
                self.assertEqual(f.getvalue(), 'Please enter a duration between 5-90.\n')

    def test_length_improper_input(self):
        """Call length improper input test"""
        self.length_improper_input_test(['hello', 10])
        self.length_improper_input_test([4, 10])
        self.length_improper_input_test([91, 10])

    def length_test_negative(self, given_answer, expected_out):
        """Test get_length with a wrong answer"""
        with patch('builtins.input', return_value=given_answer):
            length = get_length()
            self.assertNotEqual(length, expected_out)

    def test_length_unequal(self):
        """Call negative length test"""
        self.length_test_negative(11, 10)
        self.length_test_negative(9, 10)

    def genre_test(self, given_answer, expected_out):
        """Test get_genre"""
        with patch('builtins.input', return_value=given_answer):
            genre = get_genre()
            self.assertEqual(genre, expected_out)

    def test_genres(self):
        """Call genre test"""
        self.genre_test(7, 7)
        self.genre_test(6, 6)
        self.genre_test(0, 0)
        self.genre_test(1, 1)
        self.genre_test(4, 4)

    def genre_improper_input_test(self, input_stream):
        """Test handling incorrect input in get_genre"""
        with patch('builtins.input', side_effect=input_stream):
            f = io.StringIO()
            with redirect_stdout(f):
                get_genre()
                self.assertEqual(f.getvalue(), ('Enter your genre preference:'+
                                                ' \nPlease enter an integer '+
                                                'value corresponding to the ' +
                                                'following genres: \nEnter '+
                                                'your genre preference: \n'))

    def test_genre_improper_input(self):
        """Call genre improper input test"""
        self.genre_improper_input_test(['hello', 4])
        self.genre_improper_input_test([8, 4])
        self.genre_improper_input_test([-1, 4])

    def genre_test_negative(self, given_answer, expected_out):
        """Test get_genre with a wrong answer"""
        with patch('builtins.input', return_value=given_answer):
            genre = get_genre()
            self.assertNotEqual(genre, expected_out)

    def test_genre_unequal(self):
        """Call negative genre test"""
        self.genre_test_negative(1, 2)
        self.genre_test_negative(2, 3)

    def speed_test(self, given_answer, expected_out):
        """Test get_speed"""
        with patch('builtins.input', return_value=given_answer):
            speed = get_speed("start")
            self.assertEqual(speed, expected_out)

    def test_speed(self):
        """Call speed test"""
        self.speed_test(50, 50)
        self.speed_test(51, 51)
        self.speed_test(300, 300)
        self.speed_test(299, 299)
        self.speed_test(175, 175)

    def speed_improper_input_test(self, input_stream):
        """Test handling incorrect input in get_speed"""
        with patch('builtins.input', side_effect=input_stream):
            f = io.StringIO()
            with redirect_stdout(f):
                get_speed("start")
                self.assertEqual(f.getvalue(), 'Please enter a speed between 50-300 SPM\n')

    def test_speed_improper_input(self):
        """Call improper input get_speed test"""
        self.speed_improper_input_test(['hello', 175])
        self.speed_improper_input_test([49, 175])
        self.speed_improper_input_test([301, 175])

    def speed_test_negative(self, given_answer, expected_out):
        """Test get_speed with a wrong answer"""
        with patch('builtins.input', return_value=given_answer):
            speed = get_speed("start")
            self.assertNotEqual(speed, expected_out)

    def test_speed_unequal(self):
        """Call negative length test"""
        self.speed_test_negative(100, 101)
        self.speed_test_negative(101, 102)
