#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation
      of the City class."""

    def test_no_args_instantiates(self):
        """Test that City can be instantiated
          with no arguments."""
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        """Test that a new City instance is
          stored in the objects dictionary."""
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test that the id attribute of City
          is a public string instance."""
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        """Test that the created_at attribute
          of City is a public datetime instance."""
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test that the updated_at attribute
          of City is a public datetime instance."""
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        """Test that state_id is a public class
          attribute of City."""
        cy = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

    def test_name_is_public_class_attribute(self):
        """Test that name is a public class
          attribute of City."""
        cy = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)

    def test_two_cities_unique_ids(self):
        """Test that two instances of City
          have different ids."""
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_two_cities_different_created_at(self):
        """Test that two instances of City
          have different created_at timestamps."""
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.created_at, cy2.created_at)

    def test_two_cities_different_updated_at(self):
        """Test that two instances of City
          have different updated_at timestamps."""
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.updated_at, cy2.updated_at)

    def test_str_representation(self):
        """Test the __str__ representation of City."""
        dt = datetime.today()
        dt_repr = repr(dt)
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        cystr = cy.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_args_unused(self):
        """Test that City doesn't use any
          arguments passed to it."""
        cy = City(None)
        self.assertNotIn(None, cy.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test that City can be instantiated
          with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        cy = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(cy.id, "345")
        self.assertEqual(cy.created_at, dt)
        self.assertEqual(cy.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test that City raises a TypeError when
          instantiated with None keyword arguments."""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """
    Unit tests for the save method of the City class.
    """

    @classmethod
    def setUp(cls):
        """
        Set up the test case by renaming the
          file.json to tmp (if it exists).
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """
        Clean up the test case by removing file.json
          (if it exists) and renaming tmp to file.json.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_ones_save(self):
        """
        Test that the save method updates the
          updated_at attribute of City.
        """
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        self.assertLess(first_updated_at, cy.updated_at)

    def test_two_saves(self):
        """
        Test that the save method updates \
        """
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        second_updated_at = cy.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cy.save()
        self.assertLess(second_updated_at, cy.updated_at)

    def test_save_with_arg(self):
        """
        Test that the save method raises a
        TypeError when called with an argument.
        """
        cy = City()
        with self.assertRaises(TypeError):
            cy.save(None)

    def test_save_updates_file(self):
        """
        Test that the save method updates
          the file.json with the city object's data.
        """
        cy = City()
        cy.save()
        cyid = "City." + cy.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """
    Unit tests for the to_dict method of
      the City class.
    """

    def test_to_dict_type(self):
        """
        Test that the to_dict method returns
          a dictionary.
        """
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """
        Test that the to_dict method returns
          a dictionary containing the correct keys.
        """
        cy = City()
        self.assertIn("id", cy.to_dict())
        self.assertIn("created_at", cy.to_dict())
        self.assertIn("updated_at", cy.to_dict())
        self.assertIn("__class__", cy.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """
        Test that the to_dict method returns a
        dictionary containing any added attributes.
        """
        cy = City()
        cy.middle_name = "Holberton"
        cy.my_number = 98
        self.assertEqual("Holberton", cy.middle_name)
        self.assertIn("my_number", cy.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """
        Test that the datetime attributes in the
          dictionary returned by to_dict are strings.
        """
        cy = City()
        cy_dict = cy.to_dict()
        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    def test_to_dict_output(self):
        """
        Test the output of the to_dict method with known inputs.
        """
        dt = datetime.today()
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(cy.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """
        Test that the to_dict method returns
          a dictionary different from the
            object's __dict__.
        """
        cy = City()
        self.assertNotEqual(cy.to_dict(), cy.__dict__)

    def test_to_dict_with_arg(self):
        """
        Test that the to_dict method raises
        a TypeError when called with an argument.
        """
        cy = City()
        with self.assertRaises(TypeError):
            cy.to_dict(None)


if __name__ == "__main__":
    unittest.main()
