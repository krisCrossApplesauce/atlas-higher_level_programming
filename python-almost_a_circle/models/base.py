#!/usr/bin/python3
"""
Write a class called Base
"""
import json


class Base():
    """ a base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes an instance of this class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return str(json.dumps(list_dictionaries))
