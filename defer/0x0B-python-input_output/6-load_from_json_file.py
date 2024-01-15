#!/usr/bin/python3
"""module that reads a utf-8 file"""


import json


def load_from_json_file(filename):
    """function that reads a utf-8 file"""
    with open(filename) as f:
        return json.load(f)
