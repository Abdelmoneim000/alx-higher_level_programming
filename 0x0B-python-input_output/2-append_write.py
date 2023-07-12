#!/usr/bin/python3

"""A module to append text into a file"""


def append_write(filename="", text=""):
    """A function that takes a filename and text
    as parameters and reutrn the value of appending
    the text into that text file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
