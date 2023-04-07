import unittest
from guestbook import GuestBook


class TestNotebook(unittest.TestCase):

    def setUp(self):
        self.book = GuestBook()

    def test_entries(self):
        self.book.new('This is my note')
        results = self.book.entries()
        self.assertEqual(results, '1: This is my note')

    def test_edit(self):
        self.book.new('This is my note')

        self.book.edit(1, 'This is an edit')

        results = self.book.entries()
        self.assertEqual(results, '1: This is an edit')

    def tearDown(self):
        self.book.notes.clear()


if __name__ == '__main__':
    unittest.main()
