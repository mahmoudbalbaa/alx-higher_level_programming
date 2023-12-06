#!/usr/bin/python3
"""Module 0-lookup
Finding a list of available attributes and methods
"""


def lookup(obj):
    """Returns the lists of available attributes and methods

    Args:
        -obj: onject to look into
    """

    return dir(obj)
