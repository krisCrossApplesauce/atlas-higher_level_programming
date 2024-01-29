#!/usr/bin/python3
"""
unittest for /models/base.py
"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """ unittest for Base class """

    def test_id(self):
        """
        Testing that Base():
        - automatically assigns an ID
        - automatically assigns ID's incrementally
        - assigns a given ID
        """
        b1 = Base()
        b2 = Base()
        b89 = Base(89)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b89.id, 89)
        self.assertEqual(b3.id, 3)
