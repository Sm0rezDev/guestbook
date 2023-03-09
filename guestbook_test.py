import os
import unittest
from guestbook import GuestBook


class TestNotebook(unittest.TestCase):
    
    def setUp(self):
        self.book = GuestBook()
    
    def test_new(self):
        self.book.new('This is my note')
    
    def test_entries(self):
        results = self.book.entries()
        print(results)

        # self.assertEqual(results, '0: This is my note')


if __name__ == '__main__':
    unittest.main()
