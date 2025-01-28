# recursion unit test

from recursion import factorial
import unittest

class RecursionTest(unittest.TestCase):
  def testFactorial(self):
    self.assertEqual( factorial(9), 362_880, "factorial(9) != 362_880" )