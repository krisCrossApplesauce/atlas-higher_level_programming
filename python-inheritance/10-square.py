#!/usr/bin/python3
""" Square class (inherits from Rectangle which inherits from BaseGeometry """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ it's a square (wow!)"""

    def __init__(self, size):
        """ initializes the Square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ area of square obj """
        return self.__size * self.__size
