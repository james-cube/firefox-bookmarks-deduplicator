import unittest
from firefox_bookmarks_deduplicator import file_operations

class FileLoadTestSuite(unittest.TestCase):

    def test_file_load(self):
        bookmarks_object = file_operations.load_bookmarks_file("tests/testcase1.json")
        self.assertEqual(bookmarks_object.get("root"), "placesRoot")
        self.assertEqual(len(bookmarks_object.get("children")), 3)


if __name__ == '__main__':
    unittest.main() 
