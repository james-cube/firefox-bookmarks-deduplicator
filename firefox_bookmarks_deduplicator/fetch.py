def get_bookmarks_from(bookmarks_object, source):
    bookmarks_groups = bookmarks_object.get("children")
    for bookmarks_group in bookmarks_groups:
        if bookmarks_group.get("root") == source:
            return bookmarks_group.get("children")
    return []
    
def get_bookmarks_from_toolbar(bookmarks_object):
    return get_bookmarks_from(bookmarks_object, "toolbarFolder")

def get_bookmarks_from_menu(bookmarks_object):
    return get_bookmarks_from(bookmarks_object, "bookmarksMenuFolder")

def get_bookmarks_from_other(bookmarks_object):
    return get_bookmarks_from(bookmarks_object, "unfiledBookmarksFolder") 
