#!/usr/bin/python3
"""
A Module as a checker for classes instances
"""


def is_same_class(obj, a_class):
    """A function that returns True if the object is an instance of the mentioned class"""
    return (type(obj) == a_class)
