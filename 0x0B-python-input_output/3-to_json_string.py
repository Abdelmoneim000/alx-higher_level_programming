#!/usr/bin/python3
import json
"""A module to represent an object as json notation"""


def to_json_string(my_obj):
    """
    A function that takes an object as a string
    and returns the fvalue of serializing that object
    """
    return json.dumps(my_obj)
