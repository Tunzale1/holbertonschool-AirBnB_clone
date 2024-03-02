#!/usr/bin/python3
"""Base class tests"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ test BaseModel class """
    def setUp(self):
        self.instance = BaseModel()

    def test_init(self):
        """ test init """
        self.assertIsInstance(self.instance, BaseModel)
        self.assertTrue(hasattr(self.instance, "id"))
        self.assertTrue(hasattr(self.instance, "created_at"))
        self.assertTrue(hasattr(self.instance, "updated_at"))
        self.assertIsInstance(self.instance.id, str)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_dict(self):
        """ test to_dict method """
        obj = self.instance
        dic = obj.to_dict()
        self.assertIsInstance(dic, dict)
        self.assertEqual(dic['id'], obj.id)
        self.assertEqual(dic['created_at'], obj.created_at.isoformat())
        self.assertEqual(dic['updated_at'], obj.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
