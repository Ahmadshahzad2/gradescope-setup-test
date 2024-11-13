import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility, number
from ex1 import mid


class TestComplex(unittest.TestCase):
    @weight(2)
    @visibility('after_due_date')
    @number("2.1")
    def test_even_length_string(self):
        """Test with an even-length string"""
        result = mid("abcd")
        self.assertEqual(result, "")

    @weight(2)
    @visibility('after_due_date')
    @number("2.2")
    def test_odd_length_string(self):
        """Test with an odd-length string"""
        result = mid("abcde")
        self.assertEqual(result, "c")

    @weight(2)
    @number("2.3")
    def test_long_odd_length_string(self):
        """Test with a long odd-length string"""
        result = mid("abcdefghij")
        self.assertEqual(result, "")

    @weight(2)
    @number("2.4")
    def test_long_even_length_string(self):
        """Test with a long even-length string"""
        result = mid("abcdefghijklmno")
        self.assertEqual(result, "h")