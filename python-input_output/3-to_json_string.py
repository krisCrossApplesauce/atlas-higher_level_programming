#!/usr/bin/python3
"""
write a func that returns the JSON representation of an obj (str)
"""
import json


def to_json_string(my_obj):
    """ returns JSON representation of an object """
    return json.dumps(my_obj)
