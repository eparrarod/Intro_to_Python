import unittest

from Assessment.Exercise_2.main import speeding


class TestCase(unittest.TestCase):
    def test_speed_no_birthday(self):
        self.assertEqual("No Ticket", speeding(1, False), msg="1 is not fast")
        self.assertEqual("No Ticket", speeding(59, False), msg="59 is not that fast")
        self.assertEqual("No Ticket", speeding(60, False), msg="60 is not fast")
        self.assertEqual("Small Ticket", speeding(61, False), msg="61 is fast")
        self.assertEqual("Small Ticket", speeding(62, False), msg="70 is fast")
        self.assertEqual("Small Ticket", speeding(79, False), msg="79 is fast")
        self.assertEqual("Small Ticket", speeding(80, False), msg="80 is fast")
        self.assertEqual("Big Ticket", speeding(81, False), msg="81 is Too fast")
        self.assertEqual("Big Ticket", speeding(120, False), msg="120 is Too fast")

    def test_speed_birthday(self):
        self.assertEqual("No Ticket", speeding(1, True), msg="1 is not fast")
        self.assertEqual("No Ticket", speeding(59, True), msg="59 is not that fast")
        self.assertEqual("No Ticket", speeding(60, True), msg="60 is not that fast on your birthday")
        self.assertEqual("No Ticket", speeding(61, True), msg="61 is not fast on your birthday")
        self.assertEqual("No Ticket", speeding(61, True), msg="65 is not fast on your birthday")
        self.assertEqual("Small Ticket", speeding(66, True), msg="66 is fast even on your birthday")
        self.assertEqual("Small Ticket", speeding(70, True), msg="70 is fast even on your birthday")
        self.assertEqual("Small Ticket", speeding(79, True), msg="79 is fast on your birthday")
        self.assertEqual("Small Ticket", speeding(80, True), msg="80 is fast on your birthday")
        self.assertEqual("Small Ticket", speeding(81, True), msg="81 is fast on your birthday")
        self.assertEqual("Small Ticket", speeding(85, True), msg="85 is fast on your birthday")
        self.assertEqual("Big Ticket", speeding(86, True), msg="86 is too fast on your birthday")
        self.assertEqual("Big Ticket", speeding(120, True), msg="120 is Too fast")
