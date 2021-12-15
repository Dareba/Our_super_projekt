from unittest import TestCase
from main import *

class Test(TestCase):
    def test_add(self):
        self.assertEqual(add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(subtract(2, 2), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 5), 10)

    def test_divide(self):
        self.assertEqual(divide(20, 2), 10)
        self.raise

    def test_factorial(self):
        self.test_factorial(factorial(3), 6)
