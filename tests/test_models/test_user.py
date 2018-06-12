#!/user/bin/env python3
"""Module Test Case for Additional Classes"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
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

if __name__ == '__main__':
    unittest.main()
