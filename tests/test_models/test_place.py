#!/usr/bin/python3
"""Place model test"""


import unittest
from models.place import Place


class TestPlaceModel(unittest.TestCase):
    def setUp(self):
        self.place = Place()
        self.place.city_id = "1"
        self.place.user_id = "1"
        self.place.name = "Lankaran"
        self.place.description = "Lemon"
        self.place.number_rooms = 1
        self.place.number_bathrooms = 1
        self.place.max_guest = 1
        self.place.price_by_night = 1
        self.place.latitude = 1.1
        self.place.longitude = 1.1
        self.place.amenity_ids = []

    def test_type(self):
        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(Place.user_id, str)
        self.assertIsInstance(Place.name, str)
        self.assertIsInstance(Place.description, str)
        self.assertIsInstance(Place.number_rooms, int)
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertIsInstance(Place.max_guest, int)
        self.assertIsInstance(Place.price_by_night, int)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(Place.amenity_ids, object)

    def test_city_id(self):
        self.assertEqual(self.place.city_id, "1")

    def test_user_id(self):
        self.assertEqual(self.place.user_id, "1")

    def test_name(self):
        self.assertEqual(self.place.name, "Lankaran")

    def test_description(self):
        self.assertEqual(self.place.description, "Lemon")

    def test_number_rooms(self):
        self.assertEqual(self.place.number_rooms, 1)

    def test_number_bathrooms(self):
        self.assertEqual(self.place.number_bathrooms, 1)

    def test_max_guest(self):
        self.assertEqual(self.place.max_guest, 1)

    def test_price(self):
        self.assertEqual(self.place.price_by_night, 1)

    def test_latitude(self):
        self.assertEqual(self.place.latitude, 1.1)

    def test_longitude(self):
        self.assertEqual(self.place.longitude, 1.1)

    def test_amenity_ids(self):
        self.assertEqual(self.place.amenity_ids, [])