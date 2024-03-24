#!/usr/bin/env python3
"""Add all arguments to a Python list and save them to a file."""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_to_list_and_save(arguments):
    try:
        # Load existing items from the file if it exists
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list
        items = []

    # Add new arguments to the list
    items.extend(arguments)

    # Save the updated list to the file
    save_to_json_file(items, "add_item.json")

if __name__ == "__main__":
    # Exclude the script name (sys.argv[0]) from the list of arguments
    arguments = sys.argv[1:]
    add_to_list_and_save(arguments)
