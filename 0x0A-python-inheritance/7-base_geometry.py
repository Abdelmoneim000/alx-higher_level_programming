#!/usr/bin/python3
"""A module for a class that calculate the Geometry of an object"""


class BaseGeometry:
    """A class to calculate the Geometry"""

    def area(self):
        """A function to raise error message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A public method to validate the value"""
        if (type(value) != int):
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))
