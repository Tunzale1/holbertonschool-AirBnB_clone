#!/usr/bin/python3
'''FileStorage class'''


import json
import os


class FileStorage:
    '''serializes objects to a JSONfile and deserializes JSONfile to objects''' 

    __file_path = "file.json"
    __objects = {}

    def __init__(self, file_path = None):
        if file_path:
            self.__file_path = file_path
        self.reload()

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        objects = self.__objects
        my_obj = {}

        for key in objects.keys():
            my_obj[key] = objects[key].to_dict()

        with open(self.__file_path, 'w') as my_file:
            json.dump(my_obj, my_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as my_file:
                obj_dicts = json.load(my_file)
                for key, values in obj_dicts.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    instance = cls(**values)
                    self.__objects[key] = instance
