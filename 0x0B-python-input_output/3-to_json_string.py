#!/usr/bin/python3
"""module that reads a utf-8 file"""


import json


def to_json_string(my_obj):
    """function that reads a utf-8 file"""
        return json.dumps(my_obj)
