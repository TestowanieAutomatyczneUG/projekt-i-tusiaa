import unittest
from src.grade import *

class PasswordTest(unittest.TestCase):

    def setUp(self):
        self.temp = grade(5, 5)

    def test_grade_init(self):
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

    def test_grade_init_grade_string(self):
        with self.assertRaises(ValueError):
            grade("5", 5)

    def test_grade_init_scale_string(self):
        with self.assertRaises(ValueError):
            grade(5, "5")

    def test_grade_init_grade_string_scale_string(self):
        with self.assertRaises(ValueError):
            grade("5", "5")

    def test_grade_init_grade_float(self):
        with self.assertRaises(ValueError):
            grade(5.5, 5)

    def test_grade_init_scale_float(self):
        with self.assertRaises(ValueError):
            grade(5, 5.5)

    def test_grade_init_grade_float_scale_float(self):
        with self.assertRaises(ValueError):
            grade(5.5, 5.5)

    def test_grade_init_grade_bool(self):
        with self.assertRaises(ValueError):
            grade(True, 5)
    
    def test_grade_init_scale_bool(self):
        with self.assertRaises(ValueError):
            grade(5, True)

    def test_grade_init_grade_bool_scale_bool(self):
        with self.assertRaises(ValueError):
            grade(True, True)

    def test_grade_init_grade_None(self):
        with self.assertRaises(ValueError):
            grade(None, 5)

    def test_grade_init_scale_None(self):
        with self.assertRaises(ValueError):
            grade(5, None)

    def test_grade_init_grade_None_scale_None(self):
        with self.assertRaises(ValueError):
            grade(None, None)

    def test_grade_init_grade_empty(self):
        with self.assertRaises(ValueError):
            grade("", 5)

    def test_grade_init_scale_empty(self):
        with self.assertRaises(ValueError):
            grade(5, "")

    def test_grade_init_grade_empty_scale_empty(self):
        with self.assertRaises(ValueError):
            grade("", "")

    def test_grade_init_grade_array(self):
        with self.assertRaises(ValueError):
            grade([1, 2, 3], 5)

    def test_grade_init_scale_array(self):
        with self.assertRaises(ValueError):
            grade(5, [1, 2, 3])

    def test_grade_init_grade_array_scale_array(self):
        with self.assertRaises(ValueError):
            grade([1, 2, 3], [1, 2, 3])

    def test_grade_init_grade_object(self):
        with self.assertRaises(ValueError):
            grade({"grade": 5}, 5)

    def test_grade_init_scale_object(self):
        with self.assertRaises(ValueError):
            grade(5, {"scale": 5})

    def test_grade_init_grade_object_scale_object(self):
        with self.assertRaises(ValueError):
            grade({"grade": 5}, {"scale": 5})

    def test_grade_get_grade(self):
        self.assertEqual(self.temp.get_grade(), 5)

    def test_grade_get_scale(self):
        self.assertEqual(self.temp.get_scale(), 5)

    