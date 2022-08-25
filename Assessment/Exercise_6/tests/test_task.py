import unittest

from Assessment.Exercise_6.main import longest_common_sequence


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(longest_common_sequence("BCDAACD", "ACDBAC"), "CDAC",
                         msg="The longest sub-string has a length of 4")

    def test_lcs(self):
        self.assertEqual(longest_common_sequence("123456789", "123456789"), "123456789",
                         msg="The longest sub-string has a length of 9")
        self.assertEqual(longest_common_sequence("CMPTRSCNC", "CNCMPTRNC"), "CMPTR",
                         msg="The longest sub-string has a length of 5")
        self.assertEqual(longest_common_sequence("ABC", "FGH"), "", msg="There is not common sub-string")

