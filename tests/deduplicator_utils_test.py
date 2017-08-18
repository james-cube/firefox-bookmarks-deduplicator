import unittest
import io
from firefox_bookmarks_deduplicator import file_operations
from firefox_bookmarks_deduplicator import deduplicator_utils
from firefox_bookmarks_deduplicator import fetch

class FirefoxBookmarksDeduplicatorTestSuite(unittest.TestCase):

    def test_flatten_directories(self):
        bookmarks_object = file_operations.load_bookmarks_file("tests/recursion_testcase.json")
        bookmarks = fetch.get_bookmarks_from_menu(bookmarks_object)
        flattened_directories = deduplicator_utils.flatten_directories(bookmarks)
        
        self.assertEqual(len(flattened_directories), 2)
        self.assertEqual(flattened_directories[0].get("title"), "Mozilla Firefox")
        self.assertEqual(flattened_directories[1].get("title"), "Inside Mozilla Firefox")
    
    def test_flatten_bookmarks(self):
        bookmarks_object = file_operations.load_bookmarks_file("tests/recursion_testcase.json")
        bookmarks = fetch.get_bookmarks_from_menu(bookmarks_object)
        flattened_bookmarks = deduplicator_utils.flatten_bookmarks(bookmarks)
        self.assertEqual(len(flattened_bookmarks), 3)
    
    def test_has_duplicate(self):
        bookmarks_object = file_operations.load_bookmarks_file("tests/testcase1.json")
        
        bookmarks = fetch.get_bookmarks_from_other(bookmarks_object)
        duplicate = deduplicator_utils.bookmark_has_duplicate(bookmarks, bookmarks[0])
        self.assertEqual(duplicate, True)
    
    def test_duplicate_ids(self):
        bookmarks_object = file_operations.load_bookmarks_file("tests/testcase1.json")
        
        bookmarks = fetch.get_bookmarks_from_other(bookmarks_object)
        ids = deduplicator_utils.duplicate_bookmark_ids(bookmarks, bookmarks[0])
        self.assertEqual(len(ids), 2)
        self.assertEqual(ids[0], 1000)
        self.assertEqual(ids[1], 1001)
    
    def test_remove_duplicate(self):
        bookmarks_object = file_operations.load_bookmarks_file("tests/testcase1.json")
        bookmarks = fetch.get_bookmarks_from_other(bookmarks_object)
        deduplicator_utils.deduplicate(bookmarks)
        self.assertEqual(len(bookmarks), 1)#one was removed

    def test_has_directory_duplicate(self):
        bookmarks_object = file_operations.load_bookmarks_file("tests/testcase2.json")
        
        bookmarks = fetch.get_bookmarks_from_menu(bookmarks_object)
        duplicate = deduplicator_utils.directory_has_same_name(bookmarks, bookmarks[0])
        self.assertEqual(duplicate, True)
    
    def test_merge_duplicate_directories(self):
        bookmarks_object = file_operations.load_bookmarks_file("tests/testcase2.json")
        bookmarks = fetch.get_bookmarks_from_menu(bookmarks_object)
        
        deduplicator_utils.directory_merge(bookmarks)
        self.assertEqual(len(bookmarks), 1)
        self.assertEqual(bookmarks[0].get("title"), "Mozilla Firefox")
        self.assertEqual(len(bookmarks[0].get("children")), 2)

if __name__ == '__main__':
    unittest.main() 
