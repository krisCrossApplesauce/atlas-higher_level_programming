#!/usr/bin/python3
"""
Write a func that returns True
if the obj is exactly an instance of the specified class;
otherwise False
"""


def is_same_class(obj, a_class):
    """ func that checks if given obj instance of specified class """
    return isinstance(obj, a_class)
