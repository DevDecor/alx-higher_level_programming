#!/usr/bin/python3
"""Look up"""


class MyList(list):
    """My custom list"""
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        """Print a soeted list"""
        print(sorted(self))

