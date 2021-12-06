import unittest
from parameterized import parameterized, parameterized_class
from assertpy import assert_that
from src.subject import *

@parameterized_class(('namevalue', 'error'), [
    (1, ValueError),
    (1.5, ValueError),
    (True, ValueError),
    (None, ValueError),
    ("", ValueError),
    ([1,2,3], ValueError),
    ({'name': 2, 'grades': 4}, ValueError),
])
@parameterized_class(('gradevalue', 'error'), [
    (1, ValueError),
    (1.5, ValueError),
    (True, ValueError),
    (None, ValueError),
    ("", ValueError),
    ([1,2,3], ValueError),
    ({'name': 2, 'grades': 4}, ValueError),
])

class SubjectTest(unittest.TestCase):
    def setUp(self):
        self.temp = subject("Matematyka")

    def test_subject_init(self):
        assert_that(self.temp).is_not_none()

    def test_subject_init_wrong_name(self):
        assert_that(self.temp.__init__).raises(self.error).when_called_with(self.namevalue)

    def test_subject_set_name(self):
        self.temp.set_name("Informatyka")
        assert_that(self.temp.name).is_equal_to("Informatyka")

    def test_subject_set_name_wrong(self):
        assert_that(self.temp.set_name).raises(self.error).when_called_with(self.namevalue)

    def test_subject_get_name(self):
        assert_that(self.temp.get_name()).is_equal_to("Matematyka")

    def test_subject_get_grades(self):
        self.temp.add_grade(grade("1", "2"))
        assert_that(self.temp.get_grades()).is_length(1)

    def test_subject_add_grade(self):
        AddedGrade = grade("1", "2")
        self.temp.add_grade(AddedGrade)
        assert_that(self.temp.grades).contains(AddedGrade)

    @parameterized.expand([
        ("grade", ValueError),
        ("", ValueError),
        (1, ValueError),
        (1.5, ValueError),
        (True, ValueError),
        (None, ValueError),
        ([1,2,3], ValueError),
        ({grade: 1}, ValueError),
    ])
    def test_subject_add_grade_wrong(self, value, error):
        assert_that(self.temp.add_grade).raises(error).when_called_with(value)

    def test_subject_find_grade_true(self):
        self.temp.add_grade(grade("1", "2"))
        assert_that(self.temp.find_grade("1", "2")).is_instance_of(grade)

    def test_subject_find_grade_false(self):
        assert_that(self.temp.find_grade("1", "2")).is_none()

    def test_subject_find_grade_wrong_grade(self):
        assert_that(self.temp.find_grade).raises(self.error).when_called_with(self.gradevalue, 10)

    def test_subject_find_grade_wrong_scale(self):
        assert_that(self.temp.find_grade).raises(self.error).when_called_with(5, self.gradevalue)

    def test_subject_mean_from_file(self):
      fileTest = open("data/Grades_Sample")
      fileTest.read()
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(" ")
            if data[1] is not None:
                self.temp.add_grade(grade(data[0], data[1].strip("\n")))
            else:
                mean = data[0].strip("\n")
                self.assertEqual(self.temp.mean(), mean)
      fileTest.close()


    def tearDown(self):
        del self.temp