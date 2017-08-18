def flatten(bookmarks):
    result = []
    if bookmarks != None:
        for bookmark in bookmarks:
            result.append(bookmark)
            if bookmark.get("type") == "text/x-moz-place-container":
                children_bookmarks = flatten(bookmark.get("children"))
                for child in children_bookmarks:
                    result.append(child)
    return result

def flatten_bookmarks(bookmarks):
    return [b for b in flatten(bookmarks) if b.get("type") == "text/x-moz-place"]

def flatten_directories(bookmarks):
    return [b for b in flatten(bookmarks) if b.get("type") == "text/x-moz-place-container"]

def duplicate_directories(directories, directory):
    title = directory.get("title").lower()
    return [d for d in directories if d.get("title").lower() == title]

def directory_has_same_name(directories, directory):
    return len(duplicate_directories(directories, directory)) > 1

def duplicate_bookmark_ids(bookmarks, bookmark):
    flattened_bookmarks = flatten_bookmarks(bookmarks)
    return [b.get("id") for b in flattened_bookmarks if b.get("uri") == bookmark.get("uri")]

def bookmark_has_duplicate(bookmarks, bookmark):
    return len(duplicate_bookmark_ids(bookmarks, bookmark)) > 1

def directory_merge(bookmarks):
    process = True
    while process:
        flattened = flatten_directories(bookmarks)
        process = False
        
        for directory in flattened:
            if directory_has_same_name(flattened, directory):
                process = True
                current_id = directory.get("id")
                print(str(current_id) + " " + directory.get("title") + " has a duplicate")
                duplicates = duplicate_directories(flattened, directory)
                print("IDs " + str([d.get("id") for d in duplicates]))
                for dir_to_merge in duplicates:
                    merge_id = dir_to_merge.get("id")
                    if merge_id != current_id:
                        print("Merging id " + str(merge_id) + " into " + str(current_id))
                        for child in dir_to_merge.get("children"):
                            directory.get("children").append(child)
                        dir_to_merge["children"] = []
                        remove_from_tree(bookmarks, merge_id)
                break


def deduplicate(bookmarks):
    for bookmark in flatten_bookmarks(bookmarks):
        if bookmark_has_duplicate(bookmarks, bookmark):
            print(str(bookmark.get("id")) + " " + bookmark.get("uri") + " has a duplicate")
            count = 0
            for id_to_remove in duplicate_bookmark_ids(bookmarks, bookmark)[1:]:
                print("Removing id " + str(id_to_remove))
                remove_from_tree(bookmarks, id_to_remove)
                count += 1
            print("Removed " + str(count))

def remove_from_tree(bookmarks, id):
    if bookmarks != None:
        removal_index = -1
        for i in range(len(bookmarks)):
            bookmark = bookmarks[i]
            if bookmark.get("id") == id:
                removal_index = i
            if bookmark.get("type") == "text/x-moz-place-container":
                remove_from_tree(bookmark.get("children"), id)
        if removal_index >= 0:
            bookmarks.pop(removal_index)

#TODO is that used?
def get_id_path(bookmarks, id, path = []):
    if bookmarks != None:
        for bookmark in bookmarks:
            bookmark_id = bookmark.get("id")
            bookmark_type = bookmark.get("type")
            if bookmark_type == "text/x-moz-place-container":
                path.append(bookmark_id)
                tmp_path = get_id_path(bookmark.get("children"), id, path)
                if tmp_path[-1] == id:
                    return tmp_path
            elif bookmark_type == "text/x-moz-place" and bookmark_id == id:
                return path.append(bookmark_id)
    return path
