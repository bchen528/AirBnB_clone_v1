#!/usr/bin/python3
"""Unit tests for class User"""
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.user import User


class TestAdditionalClasses(unittest.TestCase):
    """testing class User"""
    @classmethod
    def setUp(cls):
        """setup instance"""
        cls.u1 = User()
        cls.u1.first_name = "Betty"
        cls.u1.last_name = "Holberton"
        cls.u1.email = "airbnb@holbertonshool.com"
        cls.u1.password = "root"

    @classmethod
    def tearDown(cls):
        """delete instance"""
        del cls.u1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """check that class of instance is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.u1.__class__, BaseModel), True)

    def test_has_attributes(self):
        """check that all class attribute have appropriate values"""
        self.assertTrue('email' in self.u1.__dict__)
        self.assertTrue('id' in self.u1.__dict__)
        self.assertTrue('created_at' in self.u1.__dict__)
        self.assertTrue('updated_at' in self.u1.__dict__)
        self.assertTrue('password' in self.u1.__dict__)
        self.assertTrue('first_name' in self.u1.__dict__)
        self.assertTrue('last_name' in self.u1.__dict__)

    def test_attribute_type(self):
        """check that all class attribute have appropriate values"""
        self.assertIsInstance(self.u1, User)
        self.assertIsInstance(self.u1, BaseModel)
        self.assertIsInstance(self.u1.email, str)
        self.assertIsInstance(self.u1.password, str)
        self.assertIsInstance(self.u1.first_name, str)
        self.assertIsInstance(self.u1.last_name, str)

    def test_checking_for_functions(self):
        """check docstrings for existing functions"""
        self.assertIsNotNone(User.__doc__)

    def test_save(self):
        """check docstrings for existing functions"""
        self.u1.save()
        self.assertNotEqual(self.u1.created_at, self.u1.updated_at)

    def test_to_dict(self):
        """check to_dict method"""
        self.assertEqual('to_dict' in dir(self.u1), True)

if __name__ == '__main__':
    unittest.main()
