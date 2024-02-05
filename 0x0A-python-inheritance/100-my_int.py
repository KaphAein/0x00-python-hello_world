#!/usr/bin/python3
"""MyInt module"""


class MyInt(int):
    """MyInt Class"""
    def __eq__(self, other):
        """equal method"""
        return int(self) != int(other)

    def __ne__(self, other):
        """not equal"""
        return int(self) == int(other)
