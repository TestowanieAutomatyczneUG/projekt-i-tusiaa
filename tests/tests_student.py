import unittest
from parameterized import parameterized_class, parameterized
from hamcrest import  *
from src.student import *
from src.Pesel_matcher import *

@parameterized_class(('value', 'error'), [
    (1, ValueError),
    (1.5, ValueError),
    (True, ValueError),
    (None, ValueError),
    ("", ValueError),
    ([1,2,3], ValueError),
    ({'name': 2, 'grades': 4}, ValueError),
])
class StudentParamerizedTest1(unittest.TestCase):
    def test_subject_init_wrong_name(self):
        assert_that(calling(student).with_args(self.value, "Kowalski", "96032687885"), raises(self.error))

    def test_subject_init_wrong_surname(self):
        assert_that(calling(student).with_args("Jan", self.value, "96032687885"), raises(self.error))


class StudentTest(unittest.TestCase):
    def setUp(self):
        self.temp = student("Jan", "Kowalski", "96032687885")

    def test_student_init(self):
        assert_that(self.temp, not_none())

    @parameterized.expand([
        ("", ValueError),
        ("123456789", ValueError),
        ("96032687886", ValueError),
        ("12345678910", ValueError),
        (96032687886, ValueError),
        (9603.2687885, ValueError),
        (True, ValueError),
        (None, ValueError),
        ([1,2,3], ValueError),
        ({'name': 2, 'grades': 4}, ValueError),
    ])
    def test_student_init_wrong_pesel(self, pesel, error):
        assert_that(calling(student).with_args("Jan", "Kowalski", pesel), raises(error))

    def test_student_get_name(self):
        assert_that(self.temp.get_name(), equal_to("Jan"))

    def test_student_get_surname(self):
        assert_that(self.temp.get_surname(), equal_to("Kowalski"))

    def test_student_get_pesel(self):
        assert_that(self.temp.get_pesel(), is_(IsValidPesel()))

    def test_student_get_remarks(self):
        assert_that(self.temp.get_remarks(), instance_of(list))

    def test_student_get_subjects(self):
        assert_that(self.temp.get_subjects(), instance_of(list))



    
    def tearDown(self):
        del self.temp