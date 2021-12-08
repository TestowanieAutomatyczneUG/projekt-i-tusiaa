from src.student import *

class register:
    def __init__(self):
        self.students = []

    def add_student(self, name: str, surname: str = None, pesel: str = None):
        if surname is None and type(name) is student:
            if self.find_by_pesel(name.pesel) is not None:
                raise ValueError("Student already exists")
            self.students.append(name)
        else:
            if self.find_by_pesel(pesel) is not None:
                raise ValueError("Student already exists")
            self.students.append(student(name, surname, pesel))

    def delete_student(self, Pesel: str):
        if not pesel(Pesel):
            raise ValueError("Invalid pesel")
        for student in self.students:
            if student.pesel == Pesel:
                self.students.remove(student)

    def find_by_pesel(self, Pesel: str):
        if not pesel(Pesel):
            raise ValueError("Invalid pesel")
        for student in self.students:
            if student.pesel == Pesel:
                return student
        return None
