#!/usr/bin/python3
"""Unit tests for class City"""
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """testing City class"""
    @classmethod
    def setUp(cls):
        """setup instance"""
        cls.c1 = City()
        cls.c1.name = "Richmond"
        cls.c1.state_id = "VA"

    @classmethod
    def tearDown(cls):
        """delete instance"""
        del cls.c1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """check that class of instance is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.c1.__class__, BaseModel), True)

    def test_has_attributes(self):
        """check that instance has all class attributes"""
        self.assertTrue('id' in self.c1.__dict__)
        self.assertTrue('created_at' in self.c1.__dict__)
        self.assertTrue('updated_at' in self.c1.__dict__)
        self.assertTrue('state_id' in self.c1.__dict__)
        self.assertTrue('name' in self.c1.__dict__)

    def test_attribute_type(self):
        """check that all class attribute have appropriate values"""
        self.assertIsInstance(self.c1, City)
        self.assertIsInstance(self.c1, BaseModel)
        self.assertIsInstance(self.c1.name, str)
        self.assertIsInstance(self.c1.state_id, str)

    def test_checking_for_functions(self):
        """check docstrings for existing functions"""
        self.assertIsNotNone(City.__doc__)

    def test_save(self):
        """check save method"""
        self.c1.save()
        self.assertNotEqual(self.c1.created_at, self.c1.updated_at)

    def test_to_dict(self):
        """check to_dict method"""
        self.assertEqual('to_dict' in dir(self.c1), True)

if __name__ == '__main__':
    unittest.main()
