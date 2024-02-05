#!/usr/bin/python3
"""add_attribute module"""


def add_attribute(obj, name, value):
    """add_attricute method"""
    if hasattr(obj, "__dict__") or \
       (hasattr(obj, "__slots") and name in obj.__slots__):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
