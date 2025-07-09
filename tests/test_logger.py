from unittest import TestCase


from pyutls import CustomLogger


class TestLogger(TestCase):

    def test_logger(self):
        logger = CustomLogger()
        logger.with_time("This test line should appear in test logs!")
