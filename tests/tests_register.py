import unittest
from parameterized import parameterized_class
from assertpy import assert_that
from src.register import *

@parameterized_class(('value', 'error'), [
    (1, ValueError),
    (1.5, ValueError),
    (True, ValueError),
    (None, ValueError),
    ("", ValueError),
    ([1,2,3], ValueError),
    ({'name': 2, 'grades': 4}, ValueError),
])
class RegisterParamerizedTest1(unittest.TestCase):
    def setUp(self):
        self.temp = register()

    def test_register_add_student_wrong_name(self):
        assert_that(self.temp.add_student).raises(self.error).when_called_with(self.value, "Kowalski", "96032687885")

    def test_register_add_student_wrong_surname(self):
        assert_that(self.temp.add_student).raises(self.error).when_called_with("Jan", self.value, "96032687885")



    def tearDown(self):
        del self.temp
    
@parameterized_class(('value', 'error'), [
    ("", ValueError),
    ("123456789", ValueError),
    ("96032687886", ValueError),
    ("96033687884", ValueError),
    ("12345678910", ValueError),
    (96032687886, ValueError),
    (9603.2687885, ValueError),
    (True, ValueError),
    (None, ValueError),
    ([1,2,3], ValueError),
    ({'name': 2, 'grades': 4}, ValueError),
])
class RegisterParamerizedTest2(unittest.TestCase):
    def setUp(self):
        self.temp = register()

    def test_register_add_student_wrong_pesel(self):
        assert_that(self.temp.add_student).raises(self.error).when_called_with("Jan", "Kowalski", self.value)

    def test_register_add_student_wrong_object(self):
        assert_that(self.temp.add_student).raises(self.error).when_called_with(self.value)



    def tearDown(self):
        del self.temp

class TestRegister(unittest.TestCase):
    def setUp(self):
        self.temp = register()

    def test_register_init(self):
        assert_that(self.temp).is_not_none()

    def test_register_add_student_by_data(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        assert_that(self.temp.get_students).is_length(1)

    def test_register_add_student_by_object(self):
        Student = student("Jan", "Kowalski", "96032687885")
        self.temp.add_student(Student)
        assert_that(self.temp.get_students).contains(Student)

    def test_register_add_student_already_exists(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        assert_that(self.temp.add_student).raises(ValueError).when_called_with("Jan", "Kowalski", "96032687885")

    def test_register_get_students(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        self.temp.add_student("Jan", "Kowalski", "94071449639")
        assert_that(self.temp.get_students).is_length(2)



    def tearDown(self):
        del self.temp