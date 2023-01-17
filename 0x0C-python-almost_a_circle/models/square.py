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

    @property
    def size(self):
        """SIze"""
        return self.width

    @size.setter
    def size(self, s):
        """Size setter"""
        self.width = s
        self.height = s

    def update(self, *args, **kwargs):
        """Updates the parameters"""
        ags = tuple(args[:])
        things = [self.id, self.size, self.x, self.y]
        if bool(args) or len(args) > 0:
            for i in range(len(ags)):
                things[i] = ags[i]
            self.id, self.size, self.x, self.y = tuple(things)
            return
        di = {
                "id": self.id,
                "size": self.height,
                "x": self.x,
                "y": self.y
            }
        for key, value in kwargs.items():
            di[key] = value
        things = di.values()
        self.id, self.size, self.x, self.y = tuple(things)
