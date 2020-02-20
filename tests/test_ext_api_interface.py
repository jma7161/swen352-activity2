from library.ext_api_interface import *;
import unittest;
import requests;
import json;
from unittest.mock import MagicMock;
from unittest.mock import patch;

def get_successful_search_json():
    with open('tests_data/successful-book-search-json.txt') as json_file:
        data = json.load(json_file);
        return data;
    
def get_successful_ebook_search_json():
    with open('tests_data/successful-ebook-search-json.txt') as json_file:
        data = json.load(json_file);
        return data;
    
class Ext_Api_Interface_Test(unittest.TestCase):
    def setUp(self):
        self.books_api = Books_API();
        self.successful_search_json = get_successful_search_json();
        self.successful_ebook_search_json = get_successful_ebook_search_json();
        self.books_by_author_title_suggest = "Isometric strength position specificity resulting from isometric and isotonic training as a determinant in performance."
        self.book_info = {'title': 'Isometric strength position specificity resulting from isometric and isotonic training as a determinant in performance.',
                          'publish_year': [1969],
                          'publisher': ['Three Rivers Press'],
                          'language': ['eng']
        };
        self.ebook_info = {
            'title': 'All your base are belong to us',
            'ebook_count': 1
        };
    def test_make_request_invalid(self):
        with patch('requests.get') as mock:
          mock.return_value.status_code = 404;
          result = self.books_api.make_request("invalid url");
          self.assertEqual(result, None);
          
    def test_make_request_connection_error(self):
        with patch('requests.get') as mock:
          mock.side_effect = requests.ConnectionError;
          result = self.books_api.make_request("connection error");
          self.assertEqual(result, None);
          
    def test_make_request_valid(self):
        with patch('requests.get') as mock:
          mock.return_value.status_code = 200;
          mock.return_value.json = get_successful_search_json;
          result = self.books_api.make_request("valid url");
          self.assertEqual(result, self.successful_search_json);
          
    def test_is_book_available_true(self):
        with patch('requests.get') as mock:
          mock.return_value.status_code = 200;
          mock.return_value.json = get_successful_search_json;
          result = self.books_api.is_book_available("available");
          self.assertEqual(result, True);
    def test_is_book_available_false(self):
        with patch('requests.get') as mock:
          mock.return_value.status_code = 400;
          result = self.books_api.is_book_available("unavailable");
          self.assertEqual(result, False);
    def test_books_by_author_no_data(self):
        with patch('requests.get') as mock:
          mock.return_value.status_code = 400;
          result = self.books_api.books_by_author("no data");
          self.assertEqual(result, []);
    def test_books_by_author(self):
        with patch('requests.get') as mock:
          mock.return_value.status_code = 200;
          mock.return_value.json = get_successful_search_json;
          result = self.books_api.books_by_author("Duane Ray Sterling");
          self.assertEqual(result, [self.books_by_author_title_suggest]);
    def test_get_book_info_no_data(self):
        with patch('requests.get') as mock:
          mock.return_value.status_code = 400;
          result = self.books_api.get_book_info("no data");
          self.assertEqual(result, []);
    def test_get_book_info(self):
        with patch('requests.get') as mock:
          mock.return_value.status_code = 200;
          mock.return_value.json = get_successful_search_json;
          result = self.books_api.get_book_info("book");
          self.assertEqual(result, [self.book_info]);
    def test_get_ebooks_no_data(self):
        with patch('requests.get') as mock:
          mock.return_value.status_code = 400;
          result = self.books_api.get_ebooks("no data");
          self.assertEqual(result, []);
    def test_get_ebooks(self):
        with patch('requests.get') as mock:
          mock.return_value.status_code = 200;
          mock.return_value.json = get_successful_ebook_search_json;
          result = self.books_api.get_ebooks("ebook");
          self.assertEqual(result, [self.ebook_info]);
    