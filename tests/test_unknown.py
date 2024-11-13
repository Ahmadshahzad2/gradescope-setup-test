import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility
from ex1 import mid


class TestUnknown(unittest.TestCase):
    @weight(2)
    @visibility('after_published')
    def test_large_string(self):
        """Evaluating a very large string for performance"""
        result = mid("a" * 1000001)  # An odd length large string
        self.assertEqual(result, "a")