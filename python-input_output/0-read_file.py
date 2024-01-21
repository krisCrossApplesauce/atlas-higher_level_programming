#!/usr/bin/python3
""" Write a func that reads a text file and prints to stdout """


def read_file(filename=""):
    """ reads file then prints to stdout """
    with open(filename, 'r') as file:
        print(file.read(), end='')
