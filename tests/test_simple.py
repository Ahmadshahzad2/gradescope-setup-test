import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from ex1 import mid


class TestSimple(unittest.TestCase):
    @weight(1)
    @number("1.1")
    def test_single_character(self):
        """Evaluate single-character string"""
        self.assertEqual(mid("a"), "a")

    @weight(1)
    @number("1.2")
    def test_empty_string(self):
        """Evaluate empty string"""
        self.assertEqual(mid(""), "")

    @weight(1)
    @number("1.3")
    def test_two_characters(self):
        """Evaluate two-character string"""
        self.assertEqual(mid("ab"), "")

    @weight(1)
    @number("1.4")
    def test_three_characters(self):
        """Evaluate three-character string"""
        self.assertEqual(mid("abc"), "b")