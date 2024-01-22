#!/usr/bin/python3
"""
write a func that writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an obj to a text file by first making it a JSON str """
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
