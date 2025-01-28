# recursion unit test

from recursion import factorial
import unittest

class RecursionTest(unittest.TestCase):
  assert( factorial(9) == 362_880 )