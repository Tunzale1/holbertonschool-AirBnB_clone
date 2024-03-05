#!/usr/bin/python3
"""User tests"""


import unittest
from models.user import User


class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_type(self):
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)

    def test_email(self):
        self.user.email = "kenan@kenan"
        self.assertEqual(self.user.email, "kenan@kenan")

    def test_password(self):
        self.user.password = "123"
        self.assertEqual(self.user.password, "123")

    def test_first_name(self):
        self.user.first_name = "Memati"
        self.assertEqual(self.user.first_name, "Memati")

    def test_last_name(self):
        self.user.last_name = "miqi"
        self.assertEqual(self.user.last_name, "miqi")