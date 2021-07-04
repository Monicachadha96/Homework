import unittest
from atmcodebreakdown1 import checkpin1

class Testcheckpin1function(unittest.TestCase):

    def correct_pin(self):
        expected = 'correct'
        result = checkpin1(user_pin1='1234')
        self.assertEqual(expected, result)

    def wrong_pin(self):
        expected = 'incorrect'
        result = checkpin1(user_pin1='0000')
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()

# to run unittests: python3 -m unittest test_red_or_blue.py