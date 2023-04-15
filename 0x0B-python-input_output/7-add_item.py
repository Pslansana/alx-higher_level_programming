#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a file"""

import sys
from typing import List
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(args: List[str]):
    """Adds all arguments to a list and saves them to a file"""

    try:
        items = load_from_json_file("add_item.json")
    except:
        items = []
    items.extend(args)
    save_to_json_file(items, "add_item.json")

if __name__ == '__main__':
    add_item(sys.argv[1:])
