#!/usr/bin/python3
"""Unit tests for class Place"""
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """testing class Place"""
    @classmethod
    def setUp(cls):
        """setup instance"""
        cls.p1 = Place()
        cls.p1.city_id = "Richmond"
        cls.p1.user_id = "VAisforLovers"
        cls.p1.name = "Blue Ridge Mountains"
        cls.p1.description = "lots of nature"
        cls.p1.number_rooms = 12
        cls.p1.number_bathrooms = 0
        cls.p1.max_guest = 50
        cls.p1.price_by_night = 100
        cls.p1.latitude = 3.0
        cls.p1.longitude = 11.0
        cls.p1.amenity_ids = []

    @classmethod
    def tearDown(cls):
        """delete instance"""
        del cls.p1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """check that class of instance is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.p1.__class__, BaseModel), True)

    def test_has_attributes(self):
        """check that instance has all class attributes"""
        self.assertTrue('id' in self.p1.__dict__)
        self.assertTrue('created_at' in self.p1.__dict__)
        self.assertTrue('updated_at' in self.p1.__dict__)
        self.assertTrue('city_id' in self.p1.__dict__)
        self.assertTrue('user_id' in self.p1.__dict__)
        self.assertTrue('name' in self.p1.__dict__)
        self.assertTrue('description' in self.p1.__dict__)
        self.assertTrue('number_rooms' in self.p1.__dict__)
        self.assertTrue('number_bathrooms' in self.p1.__dict__)
        self.assertTrue('max_guest' in self.p1.__dict__)
        self.assertTrue('price_by_night' in self.p1.__dict__)
        self.assertTrue('latitude' in self.p1.__dict__)
        self.assertTrue('longitude' in self.p1.__dict__)
        self.assertTrue('amenity_ids' in self.p1.__dict__)

    def test_attribute_type(self):
        """check that all class attribute have appropriate values"""
        self.assertIsInstance(self.p1, BaseModel)
        self.assertIsInstance(self.p1, Place)
        self.assertIsInstance(self.p1.name, str)
        self.assertIsInstance(self.p1.description, str)
        self.assertIsInstance(self.p1.number_rooms, int)
        self.assertIsInstance(self.p1.number_bathrooms, int)
        self.assertIsInstance(self.p1.max_guest, int)
        self.assertIsInstance(self.p1.price_by_night, int)
        self.assertIsInstance(self.p1.latitude, float)
        self.assertIsInstance(self.p1.longitude, float)
        self.assertIsInstance(self.p1.amenity_ids, list)

    def test_checking_for_functions(self):
        """check docstrings for existing functions"""
        self.assertIsNotNone(Place.__doc__)

    def test_save(self):
        """check save method"""
        self.p1.save()
        self.assertNotEqual(self.p1.created_at, self.p1.updated_at)

    def test_to_dict(self):
        """check to_dict method"""
        self.assertEqual('to_dict' in dir(self.p1), True)

if __name__ == '__main__':
    unittest.main()
