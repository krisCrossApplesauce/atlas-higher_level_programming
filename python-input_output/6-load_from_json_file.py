#!/usr/bin/python3
"""
write a func that creates an Object from a "JSON file"
"""
import json


def load_from_json_file(filename):
    """ creates obj from "JSON file" """
    with open(filename, 'r') as file:
        return json.load(file)
