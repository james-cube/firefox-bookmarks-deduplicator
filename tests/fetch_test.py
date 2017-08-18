import unittest
import io
from firefox_bookmarks_deduplicator import file_operations
from firefox_bookmarks_deduplicator import fetch

class SourceBookmarksLoaderTestSuite(unittest.TestCase):
    
    def test_get_bookmarks_from_toolbar(self):
        bookmarks_object = file_operations.load_bookmarks_file("tests/testcase1.json")
        toolbar_bookmarks = fetch.get_bookmarks_from_toolbar(bookmarks_object)
        self.assertEqual(len(toolbar_bookmarks), 1)
    
    def test_get_bookmarks_from_menu(self):
        bookmarks_object = file_operations.load_bookmarks_file("tests/testcase1.json")
        menu_bookmarks = fetch.get_bookmarks_from_menu(bookmarks_object)
        self.assertEqual(len(menu_bookmarks), 3)

    def test_get_bookmarks_from_other(self):
        bookmarks_object = file_operations.load_bookmarks_file("tests/testcase1.json")
        menu_bookmarks = fetch.get_bookmarks_from_other(bookmarks_object)
        self.assertEqual(len(menu_bookmarks), 2)
 
    def test_get_bookmarks_from_invalid_source(self):
        bookmarks_object = file_operations.load_bookmarks_file("tests/testcase1.json")
        empty_bookmarks = fetch.get_bookmarks_from(bookmarks_object, "bullshit")
        self.assertEqual(len(empty_bookmarks), 0)

if __name__ == '__main__':
    unittest.main() 
 
