#!/usr/bin/python3
import json
"""A module to create a JSON file with data"""


def save_to_json_file(my_obj, filename):
    """
    create a file with filename or write
    to exist file using write function
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
