import unittest

from Assessment.Exercise_5.main import taxes


class TestCase(unittest.TestCase):
    def test_taxes(self):
        self.assertEqual(taxes(2500), 250, msg="You owe 250 in taxes")
        self.assertEqual(taxes(32000), 3641, msg="You owe 250 in taxes")
        self.assertEqual(taxes(0), 0, msg="No income means no taxes")
        self.assertEqual(round(taxes(50484)), 5859, msg="You owe 4353 in taxes")
        self.assertEqual(round(taxes(9952)), 995, msg="You owe 995 in taxes")
        self.assertEqual(round(taxes(50484.59)), 58.59, msg="You owe 4353 in taxes")
        self.assertEqual(round(taxes(302254)), 49792, msg="You owe 4353 in taxes")
        self.assertEqual(round(taxes(1000000)), 264813, msg="You owe 4353 in taxes")
