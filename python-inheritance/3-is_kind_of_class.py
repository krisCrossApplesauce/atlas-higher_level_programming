#!/usr/bin/python3
"""
Write a func that returns True
if the obj is an instance of,
or if the obj is an instance of a class that inherits from,
the specified class;
otherwise False
"""


def is_kind_of_class(obj, a_class):
    """ ok this func uses isinstance """
    return isinstance(obj, a_class)
