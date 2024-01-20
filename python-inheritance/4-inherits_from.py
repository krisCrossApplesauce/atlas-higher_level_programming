#!/usr/bin/python3
""" it does whatever, I don't feel like writing these """
def inherits_from(obj, a_class):
    """ inherits but not exact instance """
    return type(obj) is not a_class and isinstance(obj, a_class)
