#!/usr/bin/env python

import unittest
import string


def reverseList(array):
    for i in range(len(array)//2):
        temp = array[i]
        array[i] = array[len(array) - 1 - i]
        array[len(array) - 1 - i] = temp
    return array


def isPalindrome(pal):
    teststring = ''
    # Start by stripping out any whitespaces or punctuation
    # When loading the letters into the array, ensure we're doing all lowercase to simplify match
    for i in range(len(pal)):
        if pal[i] in string.ascii_letters:
            teststring += pal[i].lower()

    # now to test to see if it's a palindrome
    for i in range(len(teststring)//2):
        if teststring[i] != teststring[len(teststring) - 1 - i]:
            return False
    return True


def coins(change):
    coinsizes = [ 25, 10, 5, 1 ]
    changecoins = []
    for i in range(len(coinsizes)):
        changecoins.append(change // coinsizes[i])
        change -= coinsizes[i] * changecoins[i]
    return changecoins


def factorial(number):
    if number > 1:
        return number * factorial(number - 1)
    return number


def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)

class Tester(unittest.TestCase):
    def setUp(self):
        self.reverselist1 = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
        self.reverselist2 = [ 3.14, 6, "rANDom", 12, True, 87, 30, False, 24.369, "Jiffy" ]
        self.reverselist3 = [ 12, 14, 20, 45, 58, 62, 72, 83, 173 ]
        self.reverselist4 = [ 30, 27, 24, 21, 18, 15, 12, 9, 6, 3 ]
        self.reverselist5 = [ "January", "February", "March", "April", "May", "June",
                              "July", "August", "September", "October", "November", "December" ]

        self.palindrome1 = "Go hang a salami, I\'m a lasagna hog."
        self.palindrome2 = "I am not a palindrome."
        self.palindrome3 = "Drab as a fool, aloof as a bard."
        self.palindrome4 = "Never odd or even"
        self.palindrome5 = "She sells seashells by the sea shore!"

        self.coinages1   = 73
        self.coinages2   = 2
        self.coinages3   = 42
        self.coinages4   = 99
        self.coinages5   = 13

        self.factorial1  = 5
        self.factorial2  = 17
        self.factorial3  = 3
        self.factorial4  = 42
        self.factorial5  = 1

        self.fibonacci1  = 0
        self.fibonacci2  = 1
        self.fibonacci3  = 2
        self.fibonacci4  = 15
        self.fibonacci5  = 37


    def testReverseList(self):
        self.assertEqual(reverseList(self.reverselist1), [ 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 ])
        self.assertEqual(reverseList(self.reverselist2), [ "Jiffy", 24.369, False, 30, 87, True, 12, "rANDom", 6, 3.14 ])
        self.assertEqual(reverseList(self.reverselist3), [ 173, 83, 72, 62, 58, 45, 20, 14, 12 ])
        self.assertEqual(reverseList(self.reverselist4), [3, 6, 9, 12, 15, 18, 21, 24, 27, 30 ])
        self.assertEqual(reverseList(self.reverselist5), [ "December", "November", "October", "September", "August", "July",
                                                           "June", "May", "April", "March", "February", "January" ])

    def testPalindrome(self):
        self.assertTrue(isPalindrome(self.palindrome1))
        self.assertFalse(isPalindrome(self.palindrome2))
        self.assertTrue(isPalindrome(self.palindrome3))
        self.assertTrue(isPalindrome(self.palindrome4))
        self.assertFalse(isPalindrome(self.palindrome5))


    def testCoins(self):
        self.assertEqual(coins(self.coinages1), [2, 2, 0, 3])
        self.assertEqual(coins(self.coinages2), [0, 0, 0, 2])
        self.assertEqual(coins(self.coinages3), [1, 1, 1, 2])
        self.assertEqual(coins(self.coinages4), [3, 2, 0, 4])
        self.assertEqual(coins(self.coinages5), [0, 1, 0, 3])


    def testFactorial(self):
        self.assertEqual(factorial(self.factorial1), 120)
        self.assertEqual(factorial(self.factorial2), 355687428096000)
        self.assertEqual(factorial(self.factorial3), 6)
        self.assertEqual(factorial(self.factorial4), 1405006117752879898543142606244511569936384000000000)
        self.assertEqual(factorial(self.factorial5), 1)

    def testFibonacci(self):
        self.assertEqual(fibonacci(self.fibonacci1), 0)
        self.assertEqual(fibonacci(self.fibonacci2), 1)
        self.assertEqual(fibonacci(self.fibonacci3), 1)
        self.assertEqual(fibonacci(self.fibonacci4), 610)
        self.assertEqual(fibonacci(self.fibonacci5), 24157817)


if __name__ == '__main__':
    unittest.main()
