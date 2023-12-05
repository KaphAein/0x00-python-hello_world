#!/usr/bin/python3
"""module that reads a utf-8 file"""


def read_file(filename=""):
    """function that reads a utf-8 file"""
    with open(filename,'r' ,encoding='utf-8') as f:
        print(f.read(), end="")
