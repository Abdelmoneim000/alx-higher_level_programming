#!/usr/bin/python3


"""
A module to read file or create one if
if it doesn't exist.
"""


def write_file(filename="", text=""):
    """
    A function to read or create file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
