#!/usr/bin/python3
"""module that reads a utf-8 file"""


import json


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    arguments = sys.argv[1:]

    existing_data = load_from_json_file("add_item.json") or []

    combined_data = existing_data + arguments

    save_to_json_file(combined_data, "add_item.json")
