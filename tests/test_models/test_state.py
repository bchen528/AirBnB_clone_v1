#!/usr/bin/python3
"""Unit tests for class State"""
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """testing class State"""
    @classmethod
    def setUp(cls):
        """setup instance"""
        cls.s1 = State()
        cls.s1.name = "VA"

    @classmethod
    def tearDown(cls):
        """delete instance"""
        del cls.s1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """check that class of instance is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.s1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """check docstrings for existing functions"""
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        """check that instance has all class attributes"""
        self.assertTrue('id' in self.s1.__dict__)
        self.assertTrue('created_at' in self.s1.__dict__)
        self.assertTrue('updated_at' in self.s1.__dict__)
        self.assertTrue('name' in self.s1.__dict__)

    def test_attribute_type(self):
        """check that all class attribute have appropriate values"""
        self.assertIsInstance(self.s1, State)
        self.assertIsInstance(self.s1, BaseModel)
        self.assertEqual(type(self.s1.name), str)

    def test_save(self):
        """check save method"""
        self.s1.save()
        self.assertNotEqual(self.s1.created_at, self.s1.updated_at)

    def test_to_dict(self):
        """check to_dict method"""
        self.assertEqual('to_dict' in dir(self.s1), True)

if __name__ == '__main__':
    unittest.main()
