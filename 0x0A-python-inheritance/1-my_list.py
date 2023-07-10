#!/usr/bin/python3
"""
A module to a class that prints a list in sorted order
"""


class MyList(list):
    """A subclass to sort the list from the parent class"""

    def __init__(self):
        """inherits the list from the parent class"""
        super().__init__()

    def print_sorted(self):
        """A public method to sort the list which is inherited from the parent class"""
        print(sorted(self))
