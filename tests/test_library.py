import unittest
from unittest.mock import patch
from library.library import Library


class TestLibrary(unittest.TestCase):

    @patch("library.ext_api_interface.Books_API")
    def test_is_ebook(self, mock_books):
        mock_books.return_value.get_ebooks.return_value = [{"title": "test"}]
        library = Library()
        library.api = mock_books.return_value
        self.assertTrue(library.is_ebook("test"))

    @patch("library.ext_api_interface.Books_API")
    def test_is_ebook2(self, mock_books):
        mock_books.return_value.get_ebooks.return_value = []
        library = Library()
        library.api = mock_books.return_value
        self.assertFalse(library.is_ebook("test"))

    @patch("library.ext_api_interface.Books_API")
    def test_get_ebooks_count(self, mock_books):
        mock_books.return_value.get_ebooks.return_value = [{'title': 'test', 'ebook_count': 1}]
        library = Library()
        library.api = mock_books.return_value
        self.assertEqual(library.get_ebooks_count('test'), 1)

    @patch("library.ext_api_interface.Books_API")
    def test_is_book_by_auth(self, mock_books):
        mock_books.return_value.books_by_author.return_value = []
        library = Library()
        library.api = mock_books.return_value
        self.assertFalse(library.is_book_by_author('test_author', 'test_title'))

    @patch("library.ext_api_interface.Books_API")
    def test_is_book_by_auth2(self, mock_books):
        mock_books.return_value.books_by_author.return_value = ['test_title']
        library = Library()
        library.api = mock_books.return_value
        self.assertTrue(library.is_book_by_author('test_author', 'test_title'))

    @patch("library.ext_api_interface.Books_API")
    def test_get_languages_for_book(self, mock_books):
        mock_books.return_value.get_book_info.return_value = [{'title' : 'test', 'language' : ['test_lang']}]
        library = Library()
        library.api = mock_books.return_value
        lang_set = set()
        lang_set.update(['test_lang'])
        self.assertEqual(library.get_languages_for_book('test'), lang_set)

    @patch("library.patron.Patron")
    def test_is_book_borrowed(self, mock_patron):
        mock_patron.return_value.get_borrowed_books.return_value = ['test', 'world']
        library = Library()
        self.assertTrue(library.is_book_borrowed('test', mock_patron.return_value))

    @patch("library.patron.Patron")
    def test_is_book_borrowed2(self, mock_patron):
        mock_patron.return_value.get_borrowed_books.return_value = []
        library = Library()
        self.assertFalse(library.is_book_borrowed('test', mock_patron.return_value))

    @patch("library.library_db_interface.Library_DB")
    @patch("library.patron.Patron")
    def test_is_patron_registered(self, mock_patron, mock_db):
        mock_patron.return_value.get_memberID.return_value = 1
        mock_db.return_value.retrieve_patron.return_value = None
        library = Library()
        library.db = mock_db.return_value
        self.assertFalse(library.is_patron_registered(mock_patron.return_value))

    @patch("library.library_db_interface.Library_DB")
    @patch("library.patron.Patron")
    def test_is_patron_registered2(self, mock_patron, mock_db):
        mock_patron.return_value.get_memberID.return_value = 1
        mock_db.return_value.retrieve_patron.return_value = mock_patron.return_value
        library = Library()
        library.db = mock_db.return_value
        self.assertTrue(library.is_patron_registered(mock_patron.return_value))

    @patch("library.library_db_interface.Library_DB")
    @patch("library.patron.Patron")
    def test_register_patron(self, mock_patron, mock_db):
        mock_db.return_value.insert_patron.return_value = 1
        library = Library()
        library.db = mock_db.return_value
        self.assertEqual(library.register_patron('test_first', 'test_last', 18, 1), 1)

    @patch("library.library_db_interface.Library_DB")
    @patch("library.patron.Patron")
    def test_borrow_book(self, mock_patron, mock_db):
        mock_db.return_value.update_patron.return_value = None
        library = Library()
        library.db = mock_db.return_value
        self.assertIsNone(library.borrow_book('test', mock_patron.return_value))

    @patch("library.library_db_interface.Library_DB")
    @patch("library.patron.Patron")
    def test_return_borrow_book(self, mock_patron, mock_db):
        mock_db.return_value.update_patron.return_value = None
        library = Library()
        library.db = mock_db.return_value
        self.assertIsNone(library.return_borrowed_book('test', mock_patron.return_value))

if __name__ == '__main__':
    unittest.main()
