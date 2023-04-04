#!/usr/bin/python3
"""Defines a function that adds integers"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguements are typecasted into int before addition is perfomed.

    Raises:
        TypeError: If either a or b is not an integer or not a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
