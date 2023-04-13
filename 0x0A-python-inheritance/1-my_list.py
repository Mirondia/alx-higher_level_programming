#!/usr/bin/python3
"""
MyList class
"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list that is sorted in ascending order."""
        print(sorted(self))
