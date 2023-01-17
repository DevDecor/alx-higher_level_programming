#!/usr/bin/python3
"""Python module"""
from models.rectangle import Rectangle
"""Rectangle"""


class Square(Rectangle):
    """Class documentation"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String overloading"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
