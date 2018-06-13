#!/usr/bin/python3
"""This is a class BaseModel"""
from datetime import datetime
import uuid
import json
import models


class BaseModel:
    """class BaseModel"""
    def __init__(self, *args, **kwargs):
        """initialize attributes
        Args:
            args (int): arguments to send a non-keyworded variable
                length argument list to the function
            kwargs (dict): keyworded variable length of arguments
        """
        if kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "created_at":
                    self.created_at = datetime.strptime(kwargs[key],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs[key],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    if key != "__class__":
                        setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """creates formatted string
        Returns:
            a formatted string
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def __repr__(self):
        """creates formatted string
        Returns:
            a formatted string
        """
        return self.__str__()

    def save(self):
        """updates public instance attribute
        updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """creates a dictionary containing all keys/values of
            __dict__ of the instance
        Returns:
            dictionary containing all key/values of __dict__ of instance
        """
        a_dict = dict(self.__dict__)
#        a_dict = self.__dict__
#        a_dict = {}
#        a_dict.update(self.__dict__)
        for key in a_dict:
            if key == "id":
                a_dict[key] = self.id
            elif key == "created_at":
                a_dict[key] = self.created_at.isoformat()
            elif key == "updated_at":
                a_dict[key] = self.updated_at.isoformat()
        a_dict["__class__"] = type(self).__name__
        return a_dict
