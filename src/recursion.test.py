# recursion test

from recursion import factorial
from unittest import TestCase
import unittest

class RecursionTest(TestCase):
  def testFactorial(self):
    self.assertEqual( factorial(9), 362880, "factorial(9) != 362_880" )

if __name__ == "__main__":
  unittest.main()