#!/usr/bin/python3
"""
unittest for /models/rectangle.py
"""
from models.rectangle import Rectangle
import unittest


class testRectangle(unittest.TestCase):
    """ unittest for Rectangle class """

    def test_instance(self):
        """ Testing that Rectangle correctly initializes instances """
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r2, Rectangle)
        self.assertIsInstance(r3, Rectangle)
        self.assertIsInstance(r4, Rectangle)

    def test_typeerror(self):
        """ Testing that Rectangle raises TypeErrors when necessary """
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r2 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 2, 3, "4")
#        self.assertNotIsInstance(r1, Rectangle)
#        self.assertNotIsInstance(r2, Rectangle)
#        self.assertNotIsInstance(r3, Rectangle)
#        self.assertNotIsInstance(r4, Rectangle)

    def test_valueerror(self):
        """ Testing that Rectangle raises ValueErrors when necessary """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r5 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r6 = Rectangle(1, 2, 3, -4)
#        self.assertNotIsInstance(r1, Rectangle)
#        self.assertNotIsInstance(r2, Rectangle)
#        self.assertNotIsInstance(r3, Rectangle)
#        self.assertNotIsInstance(r4, Rectangle)
#        self.assertNotIsInstance(r5, Rectangle)
#        self.assertNotIsInstance(r6, Rectangle)

    def test_area(self):
        """ Testing that the area method of Rectangle works """
        r1 = Rectangle(3, 5)
        self.assertEqual(r1.area(), 15)
