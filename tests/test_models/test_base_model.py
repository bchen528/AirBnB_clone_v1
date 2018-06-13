#!/usr/bin/python3
"""Unit test for class BaseModel"""
import unittest
import os
import pep8
import re
import models
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """TestBase Class"""
    @classmethod
    def setUpClass(cls):
        cls.b1 = BaseModel()
        cls.b1.name = "Nick"
        cls.b1.my_number = 122

    def tearDown(self):
        """Resets the FileStore.__objects private class attribute"""
        models.storage.delete_obj()
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_style_check(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quite=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_base_instance(self):
        """b1 is an instance of BaseModel"""
        self.assertIsInstance(self.b1, BaseModel)

    def test_base_public_attributes(self):
        """Tests Public Attributes of BaseModel instances"""
        self.assertIsInstance(self.b1.id, str)
        self.assertIsInstance(self.b1.created_at, datetime)
        self.assertIsInstance(self.b1.updated_at, datetime)
        self.assertEqual(str(self.b1.created_at).split('.')[0],
                         str(self.b1.updated_at).split('.')[0])


    def test_string_and_dict_and_storage_base_model(self):
        """
            1. Correct output for a printout usage of __str__
               on a BaseModel instance
            2. Correct Class output when printed
            3. Correct Id output when printed
            4. Checks for correct conversion from a base object
               to a dictionary
            5. Correct dict conversion from object
            6. Correct dict values
            7. storage all
        """
        b1 = BaseModel()
        b1.number = 89
        b1.float_num = 89.9

        # checking if __str__ works by converting it to a string, regex
        string_output = b1.__str__()

        # Correct class
        string_model = re.findall("\\[([^[\\]]*)\\]", string_output)
        self.assertEqual('BaseModel', string_model[0])

        # Correct ID
        string_id = re.findall("\\(.*?\\)", string_output)
        self.assertEqual(string_id[0][1:-1], b1.id)

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
        # checking for models.storage.new works
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
        self.assertEqual(c_val['created_at'].split('T')[0],
                         c_val['updated_at'].split('T')[0])
        self.assertEqual(c_val['created_at'].split('T')[1],
                            c_val['updated_at'].split('T')[1])

    def test_kwargs(self):
        """Kwargs input on BaseModel instantiation"""

        b1_dict = self.b1.to_dict()
        b2 = BaseModel(**b1_dict)
        b2_dict = b2.to_dict()
        self.assertEqual(b2_dict['name'], self.b1.name)
        self.assertEqual(b2_dict['my_number'], self.b1.my_number)
        self.assertEqual(
            b2_dict['updated_at'].split('T')[0], str(
                self.b1.updated_at).split()[0])
        self.assertEqual(
            b2_dict['created_at'].split('T')[1], str(
                self.b1.created_at).split()[1])
        self.assertEqual(b2_dict['id'], self.b1.id)
        self.assertEqual(b2_dict['__class__'], type(self.b1).__name__)

    def test_errs(self):
        """More or less inputs when calling specific base methods"""
        b1 = BaseModel()
        with self.assertRaises(TypeError):
            b2 = BaseModel("I'm not a kwarge")
            b1.save("help")
            b1.to_dict("I'm not a kwarg")
            print(b1.save)

    def test_save(self):
        """check save function of BaseModel"""
        b1 = BaseModel()
        b1.save()
        self.assertNotEqual(b1.created_at, b1.updated_at)

    def test_checking_for_functions(self):
        """check existence of docstring in BaseModel functions"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        """check if attributes exists"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        """check if an instance was created upon initialization"""
        self.assertTrue(isinstance(self.b1, BaseModel))

if __name__ == '__main__':
    unittest.main()
