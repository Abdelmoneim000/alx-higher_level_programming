#!/usr/bin/python3
import json

"""
A module that converts json to string format
"""


def from_json_string(my_str):
    """
    A function that decode a json string into
    it's original type
    """
    return json.loads(my_str)
