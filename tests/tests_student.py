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
    def setUp(self):
        self.temp = student("Jan", "Kowalski", "96032687885")

    def test_student_init_wrong_name(self):
        assert_that(calling(student).with_args(self.value, "Kowalski", "96032687885"), raises(self.error))

    def test_student_init_wrong_surname(self):
        assert_that(calling(student).with_args("Jan", self.value, "96032687885"), raises(self.error))

    def test_student_set_name_wrong(self):
        assert_that(calling(self.temp.set_name).with_args(self.value), raises(self.error))

    def test_student_set_surname_wrong(self):
        assert_that(calling(self.temp.set_surname).with_args(self.value), raises(self.error))

    def test_student_add_remark_wrong(self):
        assert_that(calling(self.temp.add_remark).with_args(self.value), raises(self.error))

    def test_student_delete_remark_wrong(self):
        assert_that(calling(self.temp.delete_remark).with_args(self.value), raises(self.error))

    def test_student_change_remark_wrong(self):
        self.temp.add_remark("Test")
        assert_that(calling(self.temp.change_remark).with_args(self.value), raises(self.error))    

    def test_student_add_subject_wrong(self):
        assert_that(calling(self.temp.add_subject).with_args(self.value), raises(self.error))

    def test_student_delete_subject_wrong(self):
        assert_that(calling(self.temp.delete_subject).with_args(self.value), raises(self.error))

    def test_student_find_subject_wrong(self):
        assert_that(calling(self.temp.find_subject).with_args(self.value), raises(self.error))

    def tearDown(self):
        del self.temp

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

    def test_student_set_name(self):
        self.temp.set_name("Janusz")
        assert_that(self.temp.get_name(), equal_to("Janusz"))

    def test_student_set_surname(self):
        self.temp.set_surname("Nowak")
        assert_that(self.temp.get_surname(), equal_to("Nowak"))

    def test_student_set_pesel(self):
        self.temp.set_pesel("03241311845")
        assert_that(self.temp.get_pesel(), is_(IsValidPesel()))

    def test_student_set_pesel_int(self):
        self.temp.set_pesel(94071449639)
        assert_that(self.temp.get_pesel(), is_(IsValidPesel()))

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
    def test_student_set_pesel_wrong(self, pesel, error):
        assert_that(calling(self.temp.set_pesel).with_args(pesel), raises(error))

    def test_student_add_remark(self):
        self.temp.add_remark("Test")
        assert_that(self.temp.get_remarks(), has_item("Test"))

    def test_student_delete_remark(self):
        self.temp.add_remark("Test")
        self.temp.delete_remark("Test")
        assert_that(self.temp.get_remarks(), not(contains("Test")))

    def test_student_delete_remark_without_remark(self):
        self.temp.delete_remark("Test")
        assert_that(self.temp.get_remarks(), empty())

    def test_student_change_remark(self):
        self.temp.add_remark("Test")
        self.temp.change_remark("Test", "Test2")
        assert_that(self.temp.get_remarks(), has_item("Test2"))

    def test_student_change_remark_without_remark(self):
        self.temp.change_remark("Test", "Test2")
        assert_that(self.temp.get_remarks(), not(contains("Test")))

    def test_student_add_subject(self):
        Subject= subject("Matematyka")
        self.temp.add_subject(Subject)
        assert_that(self.temp.get_subjects(), has_item(Subject))

    def test_student_add_subject_by_name(self):
        self.temp.add_subject("Matematyka")
        assert_that(calling(self.temp.find_subject).with_args("Matematyka"), not_none())

    def test_student_add_subject_already_exists(self):
        self.temp.add_subject("Matematyka")
        assert_that(calling(self.temp.add_subject).with_args("Matematyka"), raises(ValueError))

    def test_student_add_subject_already_exists_small_big_letters(self):
        self.temp.add_subject("Matematyka")
        assert_that(calling(self.temp.add_subject).with_args("mAtematyka"), raises(ValueError))

    def test_student_delete_subject(self):
        Subject= subject("Matematyka")
        self.temp.add_subject(Subject)
        self.temp.delete_subject(Subject)
        assert_that(Subject, is_in(self.temp.get_subjects()))

    def test_student_delete_subject_by_name(self):
        self.temp.add_subject("Matematyka")
        self.temp.delete_subject("Matematyka")
        assert_that(calling(self.temp.find_subject).with_args("Matematyka"), none())

    def test_student_delete_subject_do_not_exists(self):
        Subject= subject("Matematyka")
        self.temp.delete_subject(Subject)
        assert_that(calling(self.temp.find_subject).with_args("Matematyka"), none())

    def test_student_find_subject(self):
        self.temp.add_subject("Matematyka")
        assert_that(self.temp.find_subject("Matematyka"), instance_of(subject))

    def test_student_find_subject_do_not_exists(self):
        assert_that(calling(self.temp.find_subject).with_args("Matematyka"), none())

    
    def tearDown(self):
        del self.temp