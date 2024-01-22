#!/usr/bin/python3
"""
write a class called Student
"""


class Student():
    """ student class """

    def __init__(self, first_name, last_name, age):
        """ initialization of student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves dict representation of student instance """
        if attrs is not None:
            dictionary = {}
            for attr in attrs:
                if attr in self.__dict__:
                    dictionary[attr] = self.__dict__[attr]
            return dictionary
        return self.__dict__
