#!/usr/bin/python3
"""
Write a class called Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ a square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ initializes a square instance """
        super().__init__(size, size, x, y, id)

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be > 0")
        self.size = size

    def area(self):
        """ returns the area of the Square instance """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Square instance using the char # """
        for _ in range(self.__y):
            print("")
        for _ in range(self.__width):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(self.__height):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """ assigns an arg to each attribute """
        attributes = ["id", "size", "x", "y"]
        if args is not None and len(args) > 0:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        return {
            "id": self.id,
            "size": self.__width,
            "x": self.__x,
            "y": self.__y
        }

    def __str__(self):
        """ overriding the __str__ method """
        return f"[Square] ({self.id}) {self.__x}/{self.__y} " \
            + f"- {self.__width}"

    @property
    def size(self):
        """ size getter """
        return self.__width

    @size.setter
    def size(self, size):
        """ size setter """
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__width = size
        self.__height = size

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
