#!/user/bin/env python3
"""Module Test Case for Additional Classes"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.city import City


class TestAdditionalClasses(unittest.TestCase):
    """Additional Class Test"""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_additional_classes(self):
        """ """
        c1 = City()
        c1.name = "San Francisco"
        self.assertIsInstance(c1, City)
        self.assertIsInstance(c1, BaseModel)
        self.assertIsInstance(c1.name, str)

if __name__ == '__main__':
    unittest.main()
