#!/user/bin/env python3
"""Module Test Case for Additional Classes"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.place import Place


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
        p1 = Place()
        p1.name = "My House"
        p1.description = "Place by the beach"
        p1.number_rooms = 1
        p1.number_bathrooms = 1
        p1.max_guest = 1
        p1.price_by_night = 150
        p1.latitude = 37.761262
        p1.longitude = -122.504897
        p1.amenity_ids = []
        self.assertIsInstance(p1, BaseModel)
        self.assertIsInstance(p1, Place)
        self.assertIsInstance(p1.name, str)
        self.assertIsInstance(p1.description, str)
        self.assertIsInstance(p1.number_rooms, int)
        self.assertIsInstance(p1.max_guest, int)
        self.assertIsInstance(p1.price_by_night, int)
        self.assertIsInstance(p1.latitude, float)
        self.assertIsInstance(p1.longitude, float)
        self.assertIsInstance(p1.amenity_ids, list)

if __name__ == '__main__':
    unittest.main()
