#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """MyList Class"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
