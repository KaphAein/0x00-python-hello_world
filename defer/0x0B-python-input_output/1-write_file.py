#!/usr/bin/python3
"""module that reads a utf-8 file"""


def write_file(filename="", text=""):
    """function that reads a utf-8 file"""
    with open(filename, 'w', encoding='utf-8') as f:
        count = f.write(text)
        return count
