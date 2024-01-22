#!/usr/bin/python3
"""
write a func that returns an obj (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """ opposite of to_json_string """
    return json.loads(my_str)
