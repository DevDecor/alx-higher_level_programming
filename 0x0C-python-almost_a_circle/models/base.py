#!/usr/bin/python3
"""Python module"""


class Base:
    """Python class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Python Function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
