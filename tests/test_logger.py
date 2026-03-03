import logging
from unittest import TestCase


from pyutls import CustomLogger


class TestLogger(TestCase):

    def test_logger(self):
        logger1 = CustomLogger()
        logger1.with_time("This first test line should appear in test logs!")
        logger1.with_time(
            "This debug line should NOT appear in test logs!", logging.DEBUG
        )

        logger2 = CustomLogger(level=logging.DEBUG)
        logger2.with_time(
            "This second test line should appear in test logs with DEBUG line before it."
        )
        logger2.with_time(
            "This debug line should now appear in test logs...", logging.DEBUG
        )
        logger1.with_time(
            "It wouldn't be right if a DEBUG doesn't appear above this in test logs!"
        )
