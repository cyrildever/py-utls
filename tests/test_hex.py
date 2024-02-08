from unittest import TestCase


from pyutls import from_hex, to_hex


class TestHex(TestCase):

    def test_hex(self):
        ref = "1234abcd"
        barray = from_hex(ref)
        self.assertIsNotNone(barray)
        hex = to_hex(barray)
        self.assertEqual(hex, ref)

        wrong = from_hex("not-hex-string")
        self.assertIsNone(wrong)
