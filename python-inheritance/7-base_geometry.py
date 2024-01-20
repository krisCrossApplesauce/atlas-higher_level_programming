#!/usr/bin/python3
""" BaseGeometry, but with more stuff """


class BaseGeometry():
    """ no longer empty """

    def area(self):
        """ still not implemented method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
