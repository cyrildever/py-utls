from unittest import TestCase
from .context import *
from pyutls.list import flatten


class TestFlatten(TestCase):

    def test_flatten(self):
        one = ['one']
        two = ['two']
        both = [one, two]
        flat = flatten(both)
        self.assertEqual(flat, ['one', 'two'])
