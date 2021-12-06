from src.grade import *

class subject:
    def __init__(self, name: str):
        if not name or type(name) != str:
            raise ValueError("Name must be a string")
        self.name = name
        self.grades = []

    def get_name(self):
        return self.name

    def get_grades(self):
        return self.grades

    def set_name(self, name: str):
        if not name or type(name) != str:
            raise ValueError("Name must be a string")
        self.name = name

    def add_grade(self, grade: grade):
        self.grades.append(grade)

    def find_grade(self, grade: int, scale: int):
        for i in self.grades:
            if i.get_grade() == grade and i.get_scale() == scale:
                return i

    def change_grade(self, grade: int, scale: int, new_grade: int, new_scale: int):
        if self.find_grade(grade, scale) is not None:
            self.find_grade(grade, scale).set_grade(new_grade)
            self.find_grade(grade, scale).set_scale(new_scale)

    def delete_grade(self, grade: int, scale: int):
        if self.find_grade(grade, scale) is not None:
            self.grades.remove(self.find_grade(grade, scale))

    def mean(self):
        sum = 0
        scale = 0
        for i in self.grades:
            sum += i.get_grade()*i.get_scale()
            scale += i.get_scale()
        if scale == 0:
            return 0
        return sum / scale
    