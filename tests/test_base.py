#!/user/bin/env python3
"""Module Test Case"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import re
import os
from models.engine.file_storage import FileStorage
import models

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
        models.storage.delete_obj()
        if os.path.exists('file.json'):
            os.remove('file.json')        
          
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
        
    def test_string_and_dict_and_storage_base_model(self):
        """ """
        b1 = BaseModel()
    
        # checking if __str__ method works by converting it to a string and regex
        string_output = b1.__str__()
        string_model = re.findall("\[([^[\]]*)\]", string_output)
        self.assertEqual('BaseModel', string_model[0])
        string_id = re.findall("\(.*?\)", string_output)
        self.assertEqual(string_id[0][1:-1], b1.id)
        
        # assignment of different types
        b1.number = 89
        b1.float_num = 89.9
       
        # checking if to_dict works with correct values
        b1_dict = b1.to_dict()
        self.assertEqual(b1_dict['__class__'], 'BaseModel')
        self.assertEqual(b1_dict['id'], b1.id)
        updated_at_list = b1_dict['updated_at'].split('T')
        self.assertEqual(" ".join(updated_at_list), str(b1.updated_at))
        created_at_list = b1_dict['created_at'].split('T')
        self.assertEqual(" ".join(created_at_list), str(b1.created_at))
        self.assertEqual(b1_dict['number'], 89)
        self.assertEqual(b1_dict['float_num'], 89.9)

        # checking if to_dict assigns correct values
        self.assertIsInstance(b1_dict, dict)        
        self.assertIsInstance(b1_dict['__class__'], str)
        self.assertIsInstance(b1_dict['updated_at'], str)
        self.assertIsInstance(b1_dict['created_at'], str)
        self.assertIsInstance(b1_dict['id'], str)
        self.assertIsInstance(b1_dict['number'], int)
        self.assertIsInstance(b1_dict['float_num'], float)
        
        id_check = [b1]
        i = 0
        #checking for models.storage.new works
        c_dict = models.storage.all()
        for key, value in c_dict.items():
            self.assertEqual(key.split('.')[0], 'BaseModel')
            self.assertEqual(key.split('.')[1], id_check[i].id)
            i += 1
            c_val = value.to_dict()
    
        self.assertEqual(c_val['__class__'], 'BaseModel')
        self.assertEqual(c_val['id'], b1.id)
        self.assertEqual(c_val['number'], 89) 
        self.assertEqual(c_val['float_num'], 89.9)
        self.assertEqual(c_val['created_at'].split('T')[0], c_val['updated_at'].split('T')[0])
        self.assertNotEqual(c_val['created_at'].split('T')[1], c_val['updated_at'].split('T')[1])


    def test_kwargs(self):
        b1 = BaseModel()
        b1.name = "Nick" 
        b1.my_number = 122
        
        b1_dict = b1.to_dict()
        b2 = BaseModel(**b1_dict)
        b2_dict = b2.to_dict()
        self.assertEqual(b2_dict['name'], b1.name)
        self.assertEqual(b2_dict['my_number'], b1.my_number)
        self.assertEqual(b2_dict['updated_at'].split('T')[0], str(b1.updated_at).split()[0])
        self.assertEqual(b2_dict['created_at'].split('T')[1], str(b1.created_at).split()[1])
        self.assertEqual(b2_dict['id'], b1.id)
        self.assertEqual(b2_dict['__class__'], type(b1).__name__)
if __name__ == '__main__':
    unittest.main()
