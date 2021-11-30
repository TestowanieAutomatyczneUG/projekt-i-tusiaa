import unittest
from src.grade import *

class PasswordTest(unittest.TestCase):

    def test_register_init(self):
        self.temp = grade(5, 5)
        self.assertNotEqual(self.temp, None)