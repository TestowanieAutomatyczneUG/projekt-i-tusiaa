from src.student import *

class register:
    def __init__(self):
        self.students = []

    def get_students(self):
        return self.students

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
        if type(Pesel) is student:
            for Student in self.students:
                if Student.pesel == Pesel.pesel and Student.name == Pesel.name and Student.surname == Pesel.surname:
                    self.students.remove(Student)
        else:
            if not pesel(Pesel):
                raise ValueError("Invalid pesel")
            for Student in self.students:
                if Student.pesel == Pesel:
                    self.students.remove(Student)

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

    def change_student_name(self, Pesel: str, name: str):
        if not pesel(Pesel):
            raise ValueError("Invalid pesel")
        if not name or type(name) is not str:
            raise ValueError("Invalid name")
        if self.find_by_pesel(Pesel):
            self.find_by_pesel(Pesel).set_name(name) 

    def change_student_surname(self, Pesel: str, surname: str):
        if not pesel(Pesel):
            raise ValueError("Invalid pesel")
        if not surname or type(surname) is not str:
            raise ValueError("Invalid surname")
        if self.find_by_pesel(Pesel):
            self.find_by_pesel(Pesel).set_surname(surname)

    def change_student_pesel(self, old_pesel: str, new_pesel: str):
        if not pesel(old_pesel) or not pesel(new_pesel):
            raise ValueError("Invalid pesel")
        if self.find_by_pesel(new_pesel):
            raise ValueError("Student already exists")
        if self.find_by_pesel(old_pesel):
            self.find_by_pesel(old_pesel).set_pesel(new_pesel)