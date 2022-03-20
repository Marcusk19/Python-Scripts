from lib2to3.pgen2.token import NEWLINE
import os
import json
import sys

def main():
    file_path = sys.argv[1]
    folder = sys.argv[2]
    print("Opening " + str(file_path) + "..." + "\n")

    in_file = open(str(file_path), "r")
    in_data = in_file.read()
    in_file.close()

    bookmarks_dict = json.loads(in_data)

    children = bookmarks_dict['children']
    for child in children:
        if child['title'] == "toolbar":
            toolbar = child
    
    toolbar_children = toolbar['children']
    for child in toolbar_children:
        if child['title'] == str(folder):
            reading_list = child

    bookmarks = reading_list['children']

    for bookmark in bookmarks:
        title = bookmark['title']
        uri = bookmark['uri']
        print( "- [" + title + "](" + uri + ")" )


if __name__ == "__main__":
    main()