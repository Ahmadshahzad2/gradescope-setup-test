import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags
import subprocess


class TestIntegration(unittest.TestCase):
    @weight(2)
    @tags("integration")
    def test_mid_with_odd_string(self):
        """Test mid with 'abcde'"""
        calc = subprocess.Popen('python3 -u ex1.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        output, err = calc.communicate("print(mid('abcde'))\n", 1)
        self.assertIn("c", output)

    @weight(2)
    @tags("integration")
    def test_mid_with_even_string(self):
        """Test mid with 'abcd'"""
        calc = subprocess.Popen('python3 -u ex1.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        output, err = calc.communicate("print(mid('abcd'))\n", 1)
        self.assertIn("", output)