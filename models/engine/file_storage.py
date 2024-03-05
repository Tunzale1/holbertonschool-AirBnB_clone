#!/usr/bin/python3
'''FileStorage class'''

import json
import os


class FileStorage:
    '''serializes objects to a JSONfile and deserializes JSONfile to objects'''
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        serialized_object = {}
        for key, value in self.__objects.items():
            serialized_object[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized_object, f)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                dicts = json.load(f)
                for key, value in dicts.items():
                    class_name = key.split(".")[0]
                    cls = eval(class_name)
                    instance = cls(**value)
                    self.__objects[key] = instance
