#!/usr/bin/python3
"""
write a class called Student
"""
import json


class Student():
    """ student class """

    def __init__(self, first_name, last_name, age):
        """ initialization of student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves dict representation of student instance """
        return self.__dict__
