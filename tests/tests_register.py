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

    def test_register_find_students_by_name_wrong(self):
        assert_that(self.temp.find_students_by_name).raises(self.error).when_called_with(self.value)

    def test_register_find_students_by_surname_wrong(self):
        assert_that(self.temp.find_students_by_surname).raises(self.error).when_called_with(self.value)

    def test_register_find_students_by_name_and_surname_wrong_name(self):
        assert_that(self.temp.find_students_by_name_and_surname).raises(self.error).when_called_with(self.value, "Kowalski")

    def test_register_find_students_by_name_and_surname_wrong_surname(self):
        assert_that(self.temp.find_students_by_name_and_surname).raises(self.error).when_called_with("Jan", self.value)

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

    def test_register_find_student_by_pesel_wrong(self):
        assert_that(self.temp.find_student_by_pesel).raises(self.error).when_called_with(self.value)

    def test_register_delete_student_wrong(self):
        assert_that(self.temp.delete_student).raises(self.error).when_called_with(self.value)

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

    def test_register_delete_student_by_pesel(self):
        self.temp.add_student("Jan", "Kowalski", "94071449639")
        self.temp.delete_student("94071449639")
        assert_that(self.temp.find_student_by_pesel("94071449639")).is_none()

    def test_register_delete_student_by_pesel_not_found(self):
        self.temp.delete_student("94071449639")
        assert_that(self.temp.find_student_by_pesel("94071449639")).is_none()

    def test_register_delete_student_by_object(self):
        Student = student("Jan", "Kowalski", "96032687885")
        self.temp.add_student(Student)
        self.temp.delete_student(Student)
        assert_that(self.temp.get_students).is_empty()

    def test_register_delete_student_by_object_not_found(self):
        Student = student("Jan", "Kowalski", "96032687885")
        self.temp.delete_student(Student)
        assert_that(self.temp.get_students).is_empty()

    def test_register_get_students(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        self.temp.add_student("Jan", "Kowalski", "94071449639")
        assert_that(self.temp.get_students).is_length(2)

    def test_register_find_student_by_pesel(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        assert_that(self.temp.find_student_by_pesel("96032687885")).is_instance_of(student)

    def test_register_find_student_by_pesel_not_found(self):
        assert_that(self.temp.find_student_by_pesel("94071449639")).is_none()

    def test_register_find_students_by_name(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        self.temp.add_student("Jan", "Nowak", "03241311845")
        self.temp.add_student("Jan", "Konkol", "94071449639")
        assert_that(self.temp.find_students_by_name("Jan")).is_length(3)

    def test_register_find_students_by_name_not_found(self):
        assert_that(self.temp.find_students_by_name("Jan")).is_empty()

    def test_register_find_students_by_surname(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        self.temp.add_student("Ania", "Kowalski", "03241311845")
        self.temp.add_student("Karol", "Kowalski", "94071449639")
        assert_that(self.temp.find_students_by_surname("Kowalski")).is_length(3)

    def test_register_find_students_by_surname_not_found(self):
        assert_that(self.temp.find_students_by_surname("Kowalski")).is_empty()

    def test_register_find_students_by_name_and_surname(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        self.temp.add_student("Jan", "Kowalski", "03241311845")
        assert_that(self.temp.find_students_by_name_and_surname("Jan", "Kowalski")).is_length(2)

    def test_register_find_students_by_name_and_surname_not_found(self):
        assert_that(self.temp.find_students_by_name_and_surname("Jan", "Kowalski")).is_empty()


    def tearDown(self):
        del self.temp