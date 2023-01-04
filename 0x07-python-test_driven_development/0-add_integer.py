#!/usr/bin/python3
"""My module"""


def add_integer(a, b=98):
    """This function adds two integers

    Args:
        a (int): First number
        b (int): Second number
    Raises:
        TypeError: Iro lasan
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return a + b
