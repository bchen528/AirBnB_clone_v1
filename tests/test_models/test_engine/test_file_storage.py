#!/user/bin/env python3
"""Module Test Case for FileStorage"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import re
import os
from models.engine.file_storage import FileStorage
import models


class TestFileStorage(unittest.TestCase):
    """FileStorage Test Class"""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        """TearDown for each method in TestFileStorage class"""
        models.storage.delete_obj()
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_fs_instance(self):
        """FileStorage class save checks, reload checks"""
        b1 = BaseModel()
        models.storage.save()
        self.assertEqual(os.path.exists('file.json'), True)

        models.storage.delete_obj()
        models.storage.reload()

    def test_errs(self):
        """Test most mal usage of FileStorage methods"""
        with self.assertRaises(AttributeError):
            FileStorage.__objects
            FileStorage.__File_path

        with self.assertRaises(TypeError):
            models.storage.new()
            models.storage.new(self, b1)
            models.save(b1)
            models.reload(b1)
            models.all(b1)


if __name__ == '__main__':
    unittest.main()
