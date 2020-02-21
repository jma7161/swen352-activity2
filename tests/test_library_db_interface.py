import unittest
from unittest.mock import patch
from library.library_db_interface import Library_DB
from library.patron import Patron

class Testlibrary_db_interface(unittest.TestCase):
    def setUp(self):
        with patch('tinydb.TinyDB') as mock_tinydb:
            self.lib = Library_DB()
            self.lib.db = mock_tinydb.return_value

    def test_get_patron_count(self):
        self.lib.db.all.return_value = []
        self.assertEqual(self.lib.get_patron_count(), 0)

    def test_get_all_patrons(self):
        self.lib.db.all.return_value = []
        self.assertEqual(self.lib.get_all_patrons(), [])

    @patch('library.patron.Patron')
    def test_update_patron(self, mock_patron):
        self.lib.db.update.return_value = None
        self.assertIsNone(self.lib.update_patron(mock_patron.return_value))

    def test_update_patron2(self):
        self.assertIsNone(self.lib.update_patron(None))

    def test_close_db(self):
        self.lib.db.close.return_value = None
        self.assertIsNone(self.lib.close_db())

    def test_retrieve_patron(self):
        self.lib.db.search.return_value = None
        self.assertEqual(self.lib.retrieve_patron(-1), None)

    def test_retrieve_patron2(self):
        self.lib.db.search.return_value = [{'fname' : 'john', 'lname' : 'smith', 'age' : 18, 'memberID' : 1234}]
        expected = Patron('john', 'smith', 18, 1234)
        self.assertEqual(self.lib.retrieve_patron(1234), expected)


    @patch('library.patron.Patron')
    def test_insert_patron(self, mock_patron):
        mock_patron.return_value.get_memberID.return_value = 1234
        self.lib.db.search.return_value = [{"fname": "joseph", "lname": "avendano", "age": 1, "memberID": 1234, "borrowed_books": []}]
        self.assertIsNone(self.lib.insert_patron(mock_patron.return_value))

    def test_insert_patron2(self):
        self.assertEqual(self.lib.insert_patron(None), None)

    @patch('library.patron.Patron')
    def test_insert_patron3(self, mock_patron):
        mock_patron.return_value.get_memberID.return_value = 300
        mock_patron.return_value.get_fname.return_value = 'kim'
        mock_patron.return_value.get_lname.return_value = 'stall'
        mock_patron.return_value.get_age.return_value = 20
        mock_patron.return_value.get_borrowed_books.return_value = []
        self.lib.db.search.return_value = None
        self.lib.db.insert.return_value = 300
        self.assertEqual(self.lib.insert_patron(mock_patron.return_value), 300)