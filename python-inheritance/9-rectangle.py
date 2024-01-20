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

    def area(self):
        """ implemented """
        return self.__width * self.__height

    def __str__(self):
        """ wow!! I get this now!!
        this method is called __str__ bc it means that whenever
        the arg for whatever function is being used on this class obj
        is supposed to be a str (__str__),
        this is the string that the class obj will output,
        very cool
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
