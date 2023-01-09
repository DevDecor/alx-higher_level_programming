#!/usr/bin/python3
"""Module"""


def inherits_from(obj, a_class):
    """Function"""
    if isinstance(obj, a_class) and obj is not a_class:
        return True
    return False
