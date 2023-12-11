#!/usr/bin/python3
"""Class defining base"""
import json
import csv


class Base:
    """Represents a base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base"""
        if id:
            self.id = id
        else:
             Base.__nb_objects += 1
             self.id = Base.__nb_objects
