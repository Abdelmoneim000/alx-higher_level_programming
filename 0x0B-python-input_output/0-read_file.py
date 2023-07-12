#!/usr/bin/python3

"""A module to read files"""


def read_file(filename=""):
    """A function that read file and prin it"""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line)
