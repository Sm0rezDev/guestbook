import unittest
from guestbook import GuestBook


class TestNotebook(unittest.TestCase):
    
    def setUp(self):
        self.book = GuestBook()
    
    def test_entries(self):
        self.book.new('This is my note')
        results = self.book.entries()
        self.assertEqual(results, '0: This is my note\n')

    def test_edit(self):
        self.book.new('This is my note')

        self.book.edit(0, 'This is an edit')
        
        results = self.book.entries()
        self.assertEqual(results, '0: This is an edit\n')
    
    def tearDown(self):
        self.book.notes.clear()


if __name__ == '__main__':
    unittest.main()
