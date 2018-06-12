#!/user/bin/env python3
"""Module Test Case for Additional Classes"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State


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
        s1 = State()
        s1.name = "California"
        self.assertIsInstance(s1, State)
        self.assertIsInstance(s1, BaseModel)


if __name__ == '__main__':
    unittest.main()
