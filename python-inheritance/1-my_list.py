#!/usr/bin/python3
"""
Write a class called MyList that inherits from list
"""


class MyList(list):
    """ MyList class """

    def print_sorted(self):
        """ prints the list """
        print(sorted(self))
