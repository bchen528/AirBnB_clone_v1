#!/user/bin/env python3
"""Module Test Case for Additional Classes"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity


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
        """Tests all additional classes"""
        a1 = Amenity()
        a1.name = "Jacuzzi"
        self.assertIsInstance(a1, Amenity)
        self.assertIsInstance(a1, BaseModel)
        self.assertIsInstance(a1.name, str)


if __name__ == '__main__':
    unittest.main()
