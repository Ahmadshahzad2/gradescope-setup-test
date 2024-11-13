import unittest
from gradescope_utils.autograder_utils.decorators import partial_credit
from ex1 import mid


class TestPartialCredit(unittest.TestCase):
    @partial_credit(10.0)
    def test_partial_credit_odd(self, set_score=None):
        """Partial credit for correct odd-length string handling"""
        if mid("abcde") == "c":
            set_score(10.0)
        elif mid("abcde") == "":
            set_score(5.0)
        else:
            set_score(0)