from unittest import TestCase


from pyutls import euclidean_division


class TestNumber(TestCase):

    def test_euclidean_division(self):
        numerator = 15
        denominator = 2
        quotient, remainder = euclidean_division(numerator, denominator)
        self.assertEqual(quotient, 7)
        self.assertEqual(remainder, 1)
        self.assertEqual(quotient * denominator + remainder, numerator)
        with self.assertRaises(Exception):
            euclidean_division(numerator, denominator=0)
