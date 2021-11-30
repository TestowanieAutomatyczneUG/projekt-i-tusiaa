import unittest
from src.grade import *

class PasswordTest(unittest.TestCase):

    def test_register_init(self):
        self.temp = grade(5, 5)
        self.assertNotEqual(self.temp, None)

    def test_register_init_grade_to_big(self):
        with self.assertRaises(ValueError):
            grade(10, 5)

    def test_register_init_grade_to_small(self):
        with self.assertRaises(ValueError):
            grade(-1, 5)

    def test_register_init_scale_to_big(self):
        with self.assertRaises(ValueError):
            grade(5, 20)