#!/usr/bin/python3
"""
Python package that contains
all necessary attributes.
"""


class Base:
    """
    The basic class with all basic
    Attributes.
    __nb_objects = 0 : a private attribute to
    manage all instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor function for id attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
