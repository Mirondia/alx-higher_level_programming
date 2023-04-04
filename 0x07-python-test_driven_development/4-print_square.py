#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """Print a square with the # character.

    Arg:
        size (int): size length of the square.
    Raises:
        TypeError: If either size is not an int or if size is a float and is < 0
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
