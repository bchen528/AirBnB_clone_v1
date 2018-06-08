#!/usr/bin/env python3
import json
from os import path
from models.base_model import BaseModel
""" """


class FileStorage:
    """ """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ """
        return self.__objects

    def new(self, obj):
        """ """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ """
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            f.write(json.dumps(new_dict))

    def reload(self):
        """ """
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                for key, value in json.load(f).items():
                    value = BaseModel(**value)
                    self.__objects[key] = value
