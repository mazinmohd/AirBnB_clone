#!/usr/bin/python3
"""
FileStorage - Serialization and Deserialization of Objects
"""
import json
import os.path


class FileStorage:
    """
    FileStorage Class

    This class serializes instances to a JSON file
      and deserializes JSON files to instances.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary that stores serialized objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns:
            dict: A dictionary containing all serialized objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new serialized object to the dictionary.

        Args:
            obj (BaseModel): The object to be serialized.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the objects to the JSON file.
        sda asd
        ds sadssaf
        """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to objects.
        more talk ksadnj kjsa
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review

        Models = {
            'BaseModel': BaseModel,
            'User': User,
            'Amenity': Amenity,
            'Place': Place,
            'City': City,
            'State': State,
            'Review': Review
        }

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for value in data.values():
                    class_name = value.get('__class__')
                    self.new(Models[class_name](**value))
