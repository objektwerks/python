# recursion unit test

from recursion import factorial
from unittest import TestCase

class RecursionTest(TestCase):
  def testFactorial(self):
    self.assertEqual( factorial(9), 362_880, "factorial(9) != 362_880" )