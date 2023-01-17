#!/usr/bin/python3
"""Python module"""
from models.base import Base


class Rectangle(Base):
    """Python class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Python methon"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Class method"""
        return self.__width

    @width.setter
    def width(self, w):
        """Class method"""
        if (not isinstance(w, int)):
            raise TypeError("width must be an integer")
        if w <= 0:
            raise ValueError("width must be > 0")
        self.__width = w

    @property
    def height(self):
        """Class method"""
        return self.__height

    @height.setter
    def height(self, h):
        """Class method"""
        if (not isinstance(h, int)):
            raise TypeError("height must be an integer")
        if h <= 0:
            raise ValueError("height must be > 0")
        self.__height = h

    @property
    def x(self):
        """Class method"""
        return self.__x

    @x.setter
    def x(self, p):
        """Class method"""
        if (not isinstance(p, int)):
            raise TypeError("x must be an integer")
        if p < 0:
            raise ValueError("x must be >= 0")
        self.__x = p

    @property
    def y(self):
        """Class method"""
        return self.__y

    @y.setter
    def y(self, q):
        """Class method"""
        if (not isinstance(q, int)):
            raise TypeError("y must be an integer")
        if q < 0:
            raise ValueError("y must be >= 0")
        self.__y = q

    def area(self):
        """Area of the rectangle"""
        return self.width * self.height

    def display(self):
        """display the rectangle"""
        y = 0
        for i in range(self.height + self.y):
            x = 0
            if y < self.y:
                print('')
                y = y + 1
                continue
            for j in range(self.width + self.x):
                if x < self.x:
                    print(' ', end='')
                else:
                    print('#', end='')
                x = x + 1
            y = y + 1
            print('')

    def __str__(self):
        """String"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates the parameters"""
        ags = tuple(args[:])
        things = [self.id, self.width, self.height, self.x, self.y]
        if bool(args) or len(args) > 0:
            for i in range(len(ags)):
                things[i] = ags[i]
            self.id, self.width, self.height, self.x, self.y = tuple(things)
            return
        di = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
            }
        for key, value in kwargs.items():
            di[key] = value
        things = di.values()
        self.id, self.width, self.height, self.x, self.y = tuple(things)
