#!/user/bin/env python3
"""Module Test Case for Additional Classes"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import re
import os
from models.engine.file_storage import FileStorage
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.user import User


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

        u1 = User()
        u1.email = "email"
        u1.password = "password"
        u1.first_name = "Nick"
        u1.last_name = "Teixeira"
        self.assertIsInstance(u1, User)
        self.assertIsInstance(u1, BaseModel)
        self.assertIsInstance(u1.email, str)
        self.assertIsInstance(u1.password, str)
        self.assertIsInstance(u1.first_name, str)
        self.assertIsInstance(u1.last_name, str)

        s1 = State()
        s1.name = "California"
        self.assertIsInstance(s1, State)
        self.assertIsInstance(s1, BaseModel)

        c1 = City()
        c1.name = "San Francisco"
        self.assertIsInstance(c1, City)
        self.assertIsInstance(c1, BaseModel)
        self.assertIsInstance(c1.name, str)

        a1 = Amenity()
        a1.name = "Jacuzzi"
        self.assertIsInstance(a1, Amenity)
        self.assertIsInstance(a1, BaseModel)
        self.assertIsInstance(a1.name, str)

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

        r1 = Review()
        r1.place_id = "id #"
        r1.user_id = "id #"
        r1.text = "This is a review"
        self.assertIsInstance(r1.place_id, str)
        self.assertIsInstance(r1.user_id, str)
        self.assertIsInstance(r1.text, str)


if __name__ == '__main__':
    unittest.main()
