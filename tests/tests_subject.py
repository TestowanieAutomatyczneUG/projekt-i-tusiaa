import unittest
import parameterized
from src.subject import *

class SubjectTest(unittest.TestCase):
    def setUp(self):
        self.temp = subject("Matematyka")

    def test_subject_mean_from_file(self):
      fileTest = open("data/Grades_Sample")
      fileTest.read()
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(" ")
            if data[1] is not None:
                self.temp.add_grade(data[0], data[1])
            else:
                mean = data[0]
                self.assertEqual(self.temp.mean(), mean)

      fileTest.close()