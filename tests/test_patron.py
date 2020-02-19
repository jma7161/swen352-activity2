from library.patron import *
import unittest

other = Patron("other", "otro", 4, 2345)

class PatronTest(unittest.TestCase):
    def setUp(self):
        self.patron = Patron("joseph","avendano",5,1234)
    def test_init(self):
        with self.assertRaises(Exception) as context:
            Patron("jo8", "a8", 2, 3456)
        self.assertTrue("Name should not contain numbers", context)
    def test_get_fname(self):
        self.assertEqual(self.patron.get_fname(), "joseph")
    def test_get_lname(self):
        self.assertEqual(self.patron.get_lname(),"avendano")
    def test_get_age(self):
        self.assertEqual(self.patron.get_age(), 5)
    def test_get_memberID(self):
        self.assertEqual(self.patron.get_memberID(), 1234)
    def test_get_borrowed_books(self):
        self.assertEqual(self.patron.get_borrowed_books(), [])
    def test_add_borrowed_book(self):
        self.patron.add_borrowed_book("joes book")
        self.assertEqual(self.patron.get_borrowed_books(), ["joes book"])
    def test_add_borrowed_book2(self):
        self.patron.add_borrowed_book("joes book")
        self.patron.add_borrowed_book("joes book")
        self.assertEqual(self.patron.get_borrowed_books(), ["joes book"])
    def test_return_borrowed_books(self):
        self.patron.add_borrowed_book("joes book")
        self.patron.return_borrowed_book("joes book")
        self.assertEqual(self.patron.get_borrowed_books(), [])
    def test_eq(self):
        self.assertFalse(self.patron.__eq__(other))
    def test_ne(self):
        self.assertTrue(self.patron.__ne__(other))




if __name__ == '__main__':
    unittest.main()