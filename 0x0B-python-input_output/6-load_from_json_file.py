#!/usr/bin/python3
import json

"""
A module to load from JSON files
"""

def load_from_json_file(filename):
    """
    A function that takes a filename and load it's
    content as json file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
