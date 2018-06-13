#!/usr/bin/python3
"""Unit tests for class Amenity"""
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAdditionalClasses(unittest.TestCase):
    """testing class Amenity"""
    @classmethod
    def setUp(cls):
        """setup instance"""
        cls.a1 = Amenity()
        cls.a1.name = "Gym"

    @classmethod
    def tearDown(cls):
        """delete instance"""
        del cls.a1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """check that class of instance is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.a1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """check docstrings for existing functions"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        """check that instance has all class attributes"""
        self.assertTrue('id' in self.a1.__dict__)
        self.assertTrue('created_at' in self.a1.__dict__)
        self.assertTrue('updated_at' in self.a1.__dict__)
        self.assertTrue('name' in self.a1.__dict__)

    def test_attributes_type(self):
        """check that all class attribute have appropriate values"""
        self.assertIsInstance(self.a1, Amenity)
        self.assertIsInstance(self.a1, BaseModel)
        self.assertIsInstance(self.a1.name, str)

    def test_save(self):
        """check save method"""
        self.a1.save()
        self.assertNotEqual(self.a1.created_at, self.a1.updated_at)

    def test_to_dict(self):
        """check to_dict method"""
        self.assertEqual('to_dict' in dir(self.a1), True)

if __name__ == '__main__':
    unittest.main()
