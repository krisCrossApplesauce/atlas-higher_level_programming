#!/usr/bin/python3
"""
unittest for /models/rectangle.py
"""
from models.rectangle import Rectangle
import unittest


class testRectangle(unittest.TestCase):
    """ unittest for Rectangle class """

    def test_get_set(self):
        """
        Testing that Rectangle():
        - inits correctly
        - handles Type/ValueError's
        """
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r2, Rectangle)
        self.assertIsInstance(r3, Rectangle)

        with self.assertRaises(TypeError):
            r4 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r5 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            r6 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            r7 = Rectangle(1, 2, 3, "4")

        r8 = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(r8, Rectangle)
