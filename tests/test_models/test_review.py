#!/usr/bin/python3
"""Unit tests for class Review"""
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.review import Review


class TestAmenity(unittest.TestCase):
    """testing class Amenity"""
    @classmethod
    def setUp(cls):
        """setup instance"""
        cls.r1 = Review()
        cls.r1.place_id = "Raleigh"
        cls.r1.user_id = "Greg"
        cls.r1.text = "Grade A"

    @classmethod
    def tearDownClass(cls):
        """delete instance"""
        del cls.r1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """check that class of instance is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.r1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """check docstrings for existing functions"""
        self.assertIsNotNone(Review.__doc__)

    def test_has_attributes(self):
        """check that instance has all class attributes"""
        self.assertTrue('id' in self.r1.__dict__)
        self.assertTrue('created_at' in self.r1.__dict__)
        self.assertTrue('updated_at' in self.r1.__dict__)
        self.assertTrue('place_id' in self.r1.__dict__)
        self.assertTrue('text' in self.r1.__dict__)
        self.assertTrue('user_id' in self.r1.__dict__)

    def test_attributes_types(self):
        """check that all class attribute have appropriate values"""
        self.assertIsInstance(self.r1.place_id, str)
        self.assertIsInstance(self.r1.user_id, str)
        self.assertIsInstance(self.r1.text, str)

    def test_save(self):
        """check save method"""
        self.r1.save()
        self.assertNotEqual(self.r1.created_at, self.r1.updated_at)

    def test_to_dict(self):
        """check to_dict method"""
        self.assertEqual('to_dict' in dir(self.r1), True)

if __name__ == '__main__':
    unittest.main()
