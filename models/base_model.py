#!/usr/bin/python3
"""Base class"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """_summary_
    """

    def __init__(self, *args, **kwargs):
        """_summary_
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(
                kwargs.get("created_at"), "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(
                kwargs.get("updated_at"), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """save"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """_summary_
        to dict

        Returns:
            _type_: _description_
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
