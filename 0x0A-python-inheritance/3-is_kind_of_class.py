#!/usr/bin/python3
"""A module to check wheather or not an object is an instance of the mentioned class"""


def is_kind_of_class(obj, a_class):
    """a function that returns True if the obj is instance, False otherwise"""
    return isinstance(obj, a_class)
