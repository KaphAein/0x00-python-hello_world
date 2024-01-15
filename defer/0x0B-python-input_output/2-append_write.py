#!/usr/bin/python3
"""module that reads a utf-8 file"""


def append_write(filename="", text=""):
    """function that reads a utf-8 file"""
    with open(filename, 'a', encoding='utf-8') as f:
        count = f.write(text)
        return count
