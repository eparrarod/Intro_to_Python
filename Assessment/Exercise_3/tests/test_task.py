import unittest

from Assessment.Exercise_3.main import favorite_book


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual("A by The Dictionary is my favorite book.", favorite_book("A", "The Dictionary"))
        self.assertEqual("Ulysses by James Joyce is my favorite book.", favorite_book("Ulysses", "James Joyce"))
        self.assertEqual("War and Peace by Leo Tolstoy is my favorite book.", favorite_book("War and Peace", "Leo Tolstoy"))
        self.assertEqual("Jujutsu Kaisen by Gege Akutami is my favorite book.", favorite_book("Jujutsu Kaisen", "Gege Akutami"))
