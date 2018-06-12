#!/usr/bin/python3
"""This is a class FileStorage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        Returns:
            __object dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        Args:
            obj (obj): object
        """
        FileStorage.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        a_dict = {}
        for key in FileStorage.__objects:
            a_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, mode="w",
                  encoding="utf-8") as a_file:
            json.dump(a_dict, a_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode="r",
                      encoding="utf-8") as a_file:
                a_dict = json.load(a_file)
            for key, value in a_dict.items():
                FileStorage.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
