#!/usr/bin/python3
"""
Write a class called Base
"""


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
