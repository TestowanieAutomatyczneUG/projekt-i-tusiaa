from src.subject import *
from src.Pesel_matcher import pesel

class student:
    def __init__(self, name: str, surname: str, Pesel: str):
        if type(Pesel) is int:
            Pesel = str(Pesel)
        if not pesel(Pesel):
            raise ValueError("Pesel must be valid")
        if not name or type(name) != str:
            raise ValueError("Name must be string")
        if not surname or type(surname) != str:
            raise ValueError("Surname must be string")

        self.name = name
        self.surname = surname
        self.pesel = Pesel
        self.subjects = []
        self.remarks = []

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_pesel(self):
        return self.pesel

    def get_subjects(self):
        return self.subjects

    def get_remarks(self):
        return self.remarks

    def set_name(self, name: str):
        if not name or type(name) is not str:
            raise ValueError("Name must be string")
        self.name = name

    def set_surname(self, surname: str):
        if not surname or type(surname) is not str:
            raise ValueError("Surname must be string")
        self.surname = surname
    
    def set_pesel(self, Pesel: str):
        if type(Pesel) is int:
            Pesel = str(Pesel)
        if not pesel(Pesel):
            raise ValueError("Pesel must be valid")
        self.pesel = Pesel

    def add_remark(self, remark: str):
        if not remark or type(remark) is not str:
            raise ValueError("Remark must be string")
        self.remarks.append(remark)

    def delete_remark(self, remark: str):
        if not remark or type(remark) is not str:
            raise ValueError("Remark must be string")
        self.remarks.remove(remark)

    def change_remark(self, old_remark: str, new_remark: str):
        if not old_remark or type(old_remark) is not str:
            raise ValueError("Remark must be string")
        if not new_remark or type(new_remark) is not str:
            raise ValueError("Remark must be string")
        if old_remark in self.remarks:
            self.remarks[self.remarks.index(old_remark)] = new_remark
        
        