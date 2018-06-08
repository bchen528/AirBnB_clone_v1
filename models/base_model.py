#!/usr/bin/env python3
from uuid import uuid4
from datetime import datetime
import models
"""Base Module for all Objects"""


class BaseModel:
    """BaseModel with identifying attributes of each instance"""
    def __init__(self, *args, **kwargs):
        """Initialize base objects with id, created_at and updated_at
        attributes
        Args:
            args (list): list of arguments
            kwargs (dict): dictionary of arguments
        """
        if kwargs and len(kwargs) != 0:
            a_keys = ['name', 'id', 'my_number']
            self.__dict__.update((k, v) for k, v in kwargs.items() if k in a_keys)
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Saves the updated_at time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns each object to a dictionary"""
        new_dict = {}
        new_dict.update(self.__dict__)
        new_dict['__class__'] = type(self).__name__
        for key, value in self.__dict__.items():
            if key == "created_at":
                new_dict[key] = value.isoformat()
            elif key == "updated_at":
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        return new_dict

    def __str__(self):
        """Prints out a string representation of an object"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)
