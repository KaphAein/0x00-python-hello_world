#!/usr/bin/python3
"""module that reads a utf-8 file"""


import json


def from_json_string(my_str):
    """function that reads a utf-8 file"""
    return json.loads(my_str)
