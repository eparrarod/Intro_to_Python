import unittest

from Assessment.Exercise_1.main import temp_converter

class TestCase(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(32, round(temp_converter(0), 2), msg="0 celsius is 32 F")

    def test_convert_2(self):
        self.assertEqual(round(temp_converter(120), 2), 248, msg="0 celsius is 32 F")

    def test_convert_3(self):
        self.assertEqual(round(temp_converter(5), 2), 41, msg="0 celsius is 32 F")

    def test_convert_4(self):
        self.assertEqual(round(temp_converter(7.22), 2), 45.0, msg="0 celsius is 32 F")

    def test_convert_5(self):
        self.assertEqual(round(temp_converter(32.5), 2), 90.5, msg="0 celsius is 32 F")

    def test_convert_6(self):
        self.assertEqual(73.76, round(temp_converter(23.2), 2), msg="0 celsius is 32 F")
