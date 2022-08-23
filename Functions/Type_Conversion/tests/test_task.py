import unittest

from Functions.Type_Conversion.task import convert_integer, convert_float


class TestCase(unittest.TestCase):
    def test_convert_integer(self):
        self.assertEqual(convert_integer(9), 9.0, msg="A properly converted float will have the value 9.0")

    def test_convert_float(self):
        self.assertEqual(convert_float(9.0), 9, msg="A properly converted float will have the value 9")
