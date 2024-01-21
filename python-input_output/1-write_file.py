#!/usr/bin/python3
"""
write a func that writes a str to a text file
and returns the number of chars written
"""


def write_file(filename="", text=""):
    """ writes a string to a text file """
    with open(filename, 'w') as file:
        file.write(text)
    return len(text)
