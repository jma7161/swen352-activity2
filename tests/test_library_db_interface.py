import unittest
from unittest.mock import Mock
from library.library_db_interface import Library_DB
from library.patron import Patron

newPatron = Patron("big", "boy", 99, 1234)

class Testlibrary_db_interface(unittest.TestCase):
    def setUp(self):
        self.patron = Mock()
        self.patron = Patron("joseph", "avendano", 1, 1234)
        self.lib = Library_DB()
    def test_insert_patron(self):
        self.lib.insert_patron(self.patron)
        self.assertEquals(self.patron, self.lib.retrieve_patron(1234))
    def test_get_patron_count(self):
        self.lib.insert_patron(self.patron)
        self.assertEqual(1, self.lib.get_patron_count())
    def test_get_all_patrons(self):
        self.lib.insert_patron(self.patron)
        patronList = [self.lib.convert_patron_to_db_format(self.patron)]
        self.assertEqual(patronList, self.lib.get_all_patrons())

    def test_update_patron(self):
        self.lib.insert_patron(self.patron)
        self.lib.update_patron(self.patron)
        self.assertEquals(self.patron, self.lib.retrieve_patron(1234))
        self.lib.update_patron(self.patron)
        """
    def test_close_db(self):
        self.lib.insert_patron(self.patron)
        self.lib.close_db()
        patronList = []
        self.assertEqual(patronList, self.lib.get_all_patrons())
"""