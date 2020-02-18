from library.patron import *
import unittest


class PatronTest(unittest.TestCase):
    def setUp(self):
        self.patron = Patron("joseph","avendano",5,1234)
    def test_get_fname(self):
        self.assertEqual(self.patron.get_fname(), "joseph")
    def test_get_lname(self):
        self.assertEqual(self.patron.get_lname(),"avendano")
    def test_get_age(self):
        self.assertEqual(self.patron.get_age(), 5)
    def test_get_memberID(self):
        self.assertEqual(self.patron.get_memberID(), 1234)


if __name__ == '__main__':
    unittest.main()