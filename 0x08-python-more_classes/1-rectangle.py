#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Rectangle defined"""
    def __init__(self, width=0, height=0):
        self.width, self.height = width, height
    @property
    def width(self):
        """Width of the rectangle"""
        return __width

    @width.setter
    def width(self, width):
        """Width setter"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        __width = width

    @property
    def height(self):
        """Height getter"""
        return __height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
