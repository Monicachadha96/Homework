#breakdown of one of the check pin function
#user_pin1 = '0000'
#def checkpin1(user_pin1):
#    if user_pin1 == '1234':
#        print('correct pin')
#        return 'correct'
#    else:
#        print('wrong code')
#        return 'incorrect'
#

#def main():
#    print(checkpin1(user_pin1))

#if __name__ == '__main__':
#    main()


import unittest
from atmcodebreakdown1 import checkpin1

class Testcheckpin1function(unittest.TestCase):

    def test_correct_pin(self):
        expected = 'correct'
        result = checkpin1(user_pin1='1234')
        self.assertEqual(expected, result)


def test_correct_pin(self):
    expected = 'incorrect'
    result = checkpin1(user_pin1='0000')
    self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

#breakdown of one of the withdrawl function (this would be on a seperate file, submitted together for the homework)
# balance = 100
# withdrawl = 50
# def withrawl_amount1(balance):
#         if withdrawl <= balance:
#             balance = balance - withdrawl
#             print("new balance " + str(balance))
#             return balance
#         else:
#           print('value too low')
#           return 'value too low'

#def main():
#    print(withdrawl_amount1(balance))

#if __name__ == '__main__':
#    main()

from atmcodebreakdown2 import withdrawl_amount1

class Testwithdrawlamount1function(unittest.TestCase):

    def test_under_hundred(self):
        expected = 50
        result = withdrawl_amount1(balance=50)
        self.assertEqual(expected, result)

    def test_wrong_pin(self):
        expected = 'value too low'
        result = withdrawl_amount1(balance=110)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
