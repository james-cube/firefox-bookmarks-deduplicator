import json

def load_bookmarks_file(filename):
    with open(filename) as json_data:
        return json.load(json_data)

def write_to_file(filename, output):
    with open(filename, "w") as out:
        out.write(output) 
