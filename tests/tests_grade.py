import unittest
from src.grade import *

class PasswordTest(unittest.TestCase):

    def test_grade_init(self):
        self.temp = grade(5, 5)
        self.assertNotEqual(self.temp, None)

    def test_grade_init_grade_to_big(self):
        with self.assertRaises(ValueError):
            grade(10, 5)

    def test_grade_init_grade_to_small(self):
        with self.assertRaises(ValueError):
            grade(-1, 5)

    def test_grade_init_scale_to_big(self):
        with self.assertRaises(ValueError):
            grade(5, 20)

    def test_grade_init_scale_to_small(self):
        with self.assertRaises(ValueError):
            grade(5, -1)

    def test_grade_init_grade_to_big_scale_to_big(self):
        with self.assertRaises(ValueError):
            grade(10, 20)

    def test_grade_init_grade_to_small_scale_to_small(self):
        with self.assertRaises(ValueError):
            grade(-1, -1)

    def test_grade_init_grade_to_big_scale_to_small(self):
        with self.assertRaises(ValueError):
            grade(10, -1)

    def test_grade_init_grade_to_small_scale_to_big(self):
        with self.assertRaises(ValueError):
            grade(-1, 20)

    