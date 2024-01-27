#!/usr/bin/python3
"""module that reads a utf-8 file"""


import json


def save_to_json_file(my_obj, filename):
    """function that reads a utf-8 file"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
