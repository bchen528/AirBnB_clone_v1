#!/user/bin/env python3
"""Module Test Case"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import re

class TestBase(unittest.TestCase):
    """ """
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

    def test_base_instance(self):
        """ """
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        
    def test_base_public_attributes(self):
        """ """
        b1 = BaseModel() 
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)
        self.assertEqual(str(b1.created_at).split('.')[0], str(b1.updated_at).split('.')[0]) 
        
    def test_string_base_model(self):
        """ """
        b1 = BaseModel()
        string_output = b1.__str__()
        string_model = re.findall("\[([^[\]]*)\]", string_output)
        self.assertEqual('BaseModel', string_model[0])
        string_id = re.findall("\(.*?\)", string_output)
        self.assertEqual(string_id[0][1:-1], b1.id)
        
        b1.number = 89
        b1.float_num = 89.9
        
        b1_dict = b1.to_dict()
        self.assertEqual(b1_dict['__class__'], 'BaseModel')
        self.assertEqual(b1_dict['id'], b1.id)
        updated_at_list = b1_dict['updated_at'].split('T')
        self.assertEqual(" ".join(updated_at_list), str(b1.updated_at))
        created_at_list = b1_dict['created_at'].split('T')
        self.assertEqual(" ".join(created_at_list), str(b1.created_at))

        self.assertIsInstance(b1_dict, dict)        
        self.assertIsInstance(b1_dict['__class__'], str)
        self.assertIsInstance(b1_dict['updated_at'], str)
        self.assertIsInstance(b1_dict['created_at'], str)
        self.assertIsInstance(b1_dict['id'], str)
        self.assertIsInstance(b1_dict['number'], int)
        self.assertIsInstance(b1_dict['float_num'], float)

if __name__ == '__main__':
    unittest.main()
