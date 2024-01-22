#!/usr/bin/python3
"""
write a func that returns the dict description
with simple data structure (list, dict, str, int, and bool)
for JSON serialization of an object
"""


def class_to_json(obj):
    """ a func that does stuff ,'P """
    return obj.__dict__
