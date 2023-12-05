#!/usr/bin/python3
"""module that reads a utf-8 file"""


def read_file(filename=""):
    """function that reads a utf-8 file"""
    with open("filename", encoding='utf-8') as file:
        print(file.read(), end="")
