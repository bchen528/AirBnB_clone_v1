#!/user/bin/env python3
"""Module Test Case for Additional Classes"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.review import Review


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
        r1 = Review()
        r1.place_id = "id #"
        r1.user_id = "id #"
        r1.text = "This is a review"
        self.assertIsInstance(r1.place_id, str)
        self.assertIsInstance(r1.user_id, str)
        self.assertIsInstance(r1.text, str)


if __name__ == '__main__':
    unittest.main()
