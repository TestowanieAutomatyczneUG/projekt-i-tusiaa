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
    
    def find_by_name(self, name: str):
        if not name or type(name) is not str:
            raise ValueError("Invalid name")
        students = []
        for student in self.students:
            if student.name == name:
                students.append(student)
        return students

    def find_by_surname(self, surname: str):
        if not surname or type(surname) is not str:
            raise ValueError("Invalid surname")
        students = []
        for student in self.students:
            if student.surname == surname:
                students.append(student)
        return students

    def find_by_name_and_surname(self, name: str, surname: str):
        if not name or type(name) is not str:
            raise ValueError("Invalid name")
        if not surname or type(surname) is not str:
            raise ValueError("Invalid surname")
        students = []
        for student in self.students:
            if student.name == name and student.surname == surname:
                students.append(student)
        return students
