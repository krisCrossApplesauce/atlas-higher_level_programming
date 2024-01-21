#!/usr/bin/python3
"""
write a func that appends a str at the end of a text file
and returns the number of chars added
"""


def append_write(filename="", text=""):
    """ appends a string to the end of a text file """
    with open(filename, 'a') as file:
        file.write(text)
    return len(text)
