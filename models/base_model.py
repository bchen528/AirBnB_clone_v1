#!/usr/bin/python3
"""This is a class BaseModel"""
from datetime import datetime
import uuid
import json


class BaseModel:
    """class BaseModel"""

    def __init__(self):
        """initialize attributes
        Args:
            id (str): uuid
            created_at (datetime): current datetime when instance is created
            updated_at (datetime): created time but updated every time you\
                change your object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """creates formatted string
        Returns:
            a formatted string
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates public instance attribute updated_at with current datetime
        Returns:
            updated datetime
        """
        self.updated_at = datetime.now()
        return self.updated_at

    def to_dict(self):
        """creates a dictionary containing all keys/values of
            __dict__ of the instance
        Returns:
            dictionary containing all key/values of __dict__ of instance
        """
        a_dict = {}
        a_dict.update(self.__dict__)
        for key in a_dict:
            if key == "id":
                a_dict[key] = self.id
            elif key == "created_at":
                a_dict[key] = self.created_at.isoformat()
            elif key == "updated_at":
                a_dict[key] = self.updated_at.isoformat()
        a_dict["__class__"] = type(self).__name__
        return a_dict
