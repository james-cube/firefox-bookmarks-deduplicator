import cli_parser
import json
from file_operations import load_bookmarks_file
from file_operations import write_to_file
from deduplicator_utils import deduplicate
from deduplicator_utils import directory_merge
from fetch import get_bookmarks_from_toolbar
from fetch import get_bookmarks_from_menu
from fetch import get_bookmarks_from_other

def deduplicate_and_merge_all(bookmarks_object):
    deduplicate_and_merge(get_bookmarks_from_toolbar(bookmarks_object))
    deduplicate_and_merge(get_bookmarks_from_menu(bookmarks_object))
    deduplicate_and_merge(get_bookmarks_from_other(bookmarks_object))

def deduplicate_and_merge(bookmarks):
    deduplicate(bookmarks)
    directory_merge(bookmarks)

def main():
    args = cli_parser.parse_arguments()
    bookmarks_object = load_bookmarks_file(args.file)
    deduplicate_and_merge_all(bookmarks_object)
    write_to_file(args.output, json.dumps(bookmarks_object, indent=4))
