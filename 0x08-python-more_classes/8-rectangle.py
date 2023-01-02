#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Rectangle defined"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor"""
        Rectangle.number_of_instances += 1
        self.width, self.height = width, height

    @property
    def width(self):
        """Width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Perimeter of the rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """String representation"""
        x = ""
        if self.height == 0 or self.width == 0:
            return x
        for i in range(self.height):
            for j in range(self.width):
                x = x + str(self.print_symbol)
            if i != self.height - 1:
                x = x + "\n"
        return x

    def __repr__(self):
        """Representation"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """I am Dying"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1
