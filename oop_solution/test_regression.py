import unittest
from contextlib import redirect_stdout
from io import StringIO
from oop_solution.library_oop import Library

class LibraryRegressionTests(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        with redirect_stdout(StringIO()):
            self.library.add_book(1, "Test Book", "Author", 3)
            self.library.add_book(2, "Book 2", "Author", 1)
            self.library.add_book(3, "Book 3", "Author", 1)
            self.library.add_book(4, "Book 4", "Author", 1)
            self.library.add_member(101, "Alice", "alice@example.com")
            self.library.add_member(102, "Bob", "bob@example.com")

    def action(self, method, *args):
        with redirect_stdout(StringIO()):
            return method(*args)

    def test_duplicate_borrow_does_not_decrement_stock(self):
        self.assertTrue(self.action(self.library.borrow_book, 101, 1))
        self.assertFalse(self.action(self.library.borrow_book, 101, 1))
        self.assertEqual(self.library.books[1].available_copies, 2)
        self.assertEqual(self.library.members[101].borrowed_books, [1])
        self.assertTrue(self.action(self.library.return_book, 101, 1))
        self.assertEqual(self.library.books[1].available_copies, 3)

    def test_out_of_stock_rejected(self):
        self.assertTrue(self.action(self.library.borrow_book, 101, 2))
        self.assertFalse(self.action(self.library.borrow_book, 102, 2))
        self.assertEqual(self.library.books[2].available_copies, 0)

    def test_borrow_limit(self):
        for book_id in (1, 2, 3):
            self.assertTrue(self.action(self.library.borrow_book, 101, book_id))
        self.assertFalse(self.action(self.library.borrow_book, 101, 4))
        self.assertEqual(self.library.books[4].available_copies, 1)

    def test_invalid_return_does_not_change_inventory(self):
        self.assertFalse(self.action(self.library.return_book, 101, 1))
        self.assertEqual(self.library.books[1].available_copies, 3)
        self.assertFalse(self.action(self.library.return_book, 999, 1))
        self.assertEqual(self.library.books[1].available_copies, 3)

    def test_missing_member_or_book(self):
        self.assertFalse(self.action(self.library.borrow_book, 999, 1))
        self.assertFalse(self.action(self.library.borrow_book, 101, 999))
        self.assertEqual(self.library.books[1].available_copies, 3)

if __name__ == "__main__":
    unittest.main()
