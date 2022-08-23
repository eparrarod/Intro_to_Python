import unittest

from Basics.Function_with_loop.task import less_than_ten


class TestCase(unittest.TestCase):
    def test_llt(self):
        self.assertEqual(less_than_ten(1), 10, msg="Starts at a = 1 ends after adding ones returning 10")
