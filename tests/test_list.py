from unittest import TestCase


from pyutls import flatten, chunk


class TestChunk(TestCase):

    def test_chunk(self):
        items = [1, 2, 3, 4, 5]
        chunks = chunk(items, 2)
        self.assertEqual(3, len(chunks))
        self.assertListEqual(chunks[0], [1, 2])
        self.assertListEqual(chunks[1], [3, 4])
        self.assertListEqual(chunks[2], [5])


class TestFlatten(TestCase):

    def test_flatten(self):
        one = ["one"]
        two = ["two"]
        both = [one, two]
        flat = flatten(both)
        self.assertEqual(flat, ["one", "two"])

        some_list = [1, 2, 3, 4, 5]
        chunks = chunk(some_list, 2)
        flat_list = flatten(chunks)
        self.assertEqual(some_list, flat_list)
