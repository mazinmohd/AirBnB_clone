#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests for testing insta
    ntiation of the User class."""

    def test_no_args_instantiates(self):
        """Test that User class can be
          instantiated with no arguments."""
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        """Test that a new instance of
          User is stored in objects."""
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test that the id attribute of User
          is a public string instance."""
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        """Test that the created_at attribute
          of User is a public datetime instance."""
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test that the updated_at attribute
          of User is a public datetime instance."""
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        """Test that the email attribute of
          User is a public string instance."""
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        """Test that the password attribute
          of User is a public string instance."""
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        """Test that the first_name attribute
          of User is a public string instance."""
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        """Test that the last_name attribute
          of User is a public string instance."""
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        """Test that two instances of User
          have unique ids."""
        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)

    def test_two_users_different_created_at(self):
        """Test that two instances of User
          have different created_at timestamps."""
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_users_different_updated_at(self):
        """Test that two instances of User
          have different updated_at timestamps."""
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.updated_at, us2.updated_at)

    def test_str_representation(self):
        """Test the string representation
          of User instance."""
        dt = datetime.today()
        dt_repr = repr(dt)
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        usstr = us.__str__()
        self.assertIn("[User] (123456)", usstr)
        self.assertIn("'id': '123456'", usstr)
        self.assertIn("'created_at': " + dt_repr, usstr)
        self.assertIn("'updated_at': " + dt_repr, usstr)

    def test_args_unused(self):
        """Test that User instance ign
        ores unused arguments."""
        us = User(None)
        self.assertNotIn(None, us.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test that User instance can be
          instantiated with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        us = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(us.id, "345")
        self.assertEqual(us.created_at, dt)
        self.assertEqual(us.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test that User instance raises TypeError
          when instantiated with None keyword arguments."""
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the User class."""

    @classmethod
    def setUp(self):
        """Set up the test environment
          before running the test cases."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """Clean up the test environment
          after running the test cases."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """Test that the save method updates
          the updated_at attribute of User."""
        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        self.assertLess(first_updated_at, us.updated_at)

    def test_two_saves(self):
        """Test that multiple saves update the
          updated_at attribute of User."""
        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        second_updated_at = us.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        us.save()
        self.assertLess(second_updated_at, us.updated_at)

    def test_save_with_arg(self):
        """Test that the save method raises
          TypeError when called with an argument."""
        us = User()
        with self.assertRaises(TypeError):
            us.save(None)

    def test_save_updates_file(self):
        """Test that the save method
          updates the file.json file."""
        us = User()
        us.save()
        usid = "User." + us.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict met
    hod of the User class."""

    def test_to_dict_type(self):
        """Test that the to_dict method
          returns a dictionary."""
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test that the to_dict method
          returns a dictionary with correct keys."""
        us = User()
        self.assertIn("id", us.to_dict())
        self.assertIn("created_at", us.to_dict())
        self.assertIn("updated_at", us.to_dict())
        self.assertIn("__class__", us.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test that the to_dict method
          includes added attributes."""
        us = User()
        us.middle_name = "Holberton"
        us.my_number = 98
        self.assertEqual("Holberton", us.middle_name)
        self.assertIn("my_number", us.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test that datetime attributes in
          the to_dict output are strings."""
        us = User()
        us_dict = us.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of the to_dict method."""
        dt = datetime.today()
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(us.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test that the to_dict method output
          is not equal to the __dict__ attribute."""
        us = User()
        self.assertNotEqual(us.to_dict(), us.__dict__)

    def test_to_dict_with_arg(self):
        """Test that the to_dict method raises
          TypeError when called with an argument."""
        us = User()
        with self.assertRaises(TypeError):
            us.to_dict(None)


if __name__ == "__main__":
    unittest.main()
