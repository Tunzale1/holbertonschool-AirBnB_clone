#!/usr/bin/python3
"""State model test"""


import unittest
from models.state import State

class TestStateModel(unittest.TestCase):
    def setUp(self):
        self.state = State()
        self.state.name = "Lankaran"

    def test_type(self):
        self.assertIsInstance(State.name, str)

    def test_name(self):
        self.assertEqual(self.state.name, "Lankaran")