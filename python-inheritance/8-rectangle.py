#!/usr/bin/python3
""" Rectangle class :P """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ wow, this specific shape is a rectangle """

    def __init__(self, width, height):
        """ initializing rectangle """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
