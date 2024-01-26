#!/usr/bin/python3
"""
unittest for /models/base.py
"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """ unittest for Base class """

    def test_ID(self):
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
        self.assertTrue(b1.id == 1)
        self.assertTrue(b2.id == 2)
        self.assertTrue(b89.id == 89)
        self.assertTrue(b3.id == 3)
