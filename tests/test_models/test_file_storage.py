#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:

"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
import unittest


class TestFileStorage(unittest.TestCase):
    """TestFileStorage
    test for file sot
    df"""
    # all method returns a dictionary containing all serialized objects

    def test_all_method_returns_dictionary(self):
        """test_all_method_returns_dictionary"""
        storage = FileStorage()
        obj1 = BaseModel()
        obj2 = User()
        storage.new(obj1)
        storage.new(obj2)
        result = storage.all()
        self.assertIsInstance(result, dict)
        self.assertIn(f"{obj1.__class__.__name__}.{obj1.id}", result)
        self.assertIn(f"{obj2.__class__.__name__}.{obj2.id}", result)

    # new method adds a new serialized object to the dictionary
    def test_new_method_adds_new_object(self):
        """test_new_method_adds_new_object"""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        result = storage.all()
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", result)

    def test_all_method_returns_empty_dictionary(self):
        """test_all_method_returns_empty_dictionary"""
        storage = FileStorage()
        result = storage.all()
        self.assertIsInstance(result, dict)

    def test_new_method_raises_attribute_error(self):
        """test_new_method_raises_attribute_error"""
        storage = FileStorage()
        obj = "not a BaseModel instance"
        with self.assertRaises(AttributeError):
            storage.new(obj)


if __name__ == "__main__":
    unittest.main()
