from src.subject import *
from src.Pesel_matcher import pesel

class student:
    def __init__(self, name: str, surname: str, Pesel: str):
        if type(Pesel) is int:
            Pesel = str(Pesel)
        if not pesel(Pesel):
            raise ValueError("PESEL musi być poprawny")
        if not name or type(name) != str:
            raise ValueError("Imię musi być napisem")
        if not surname or type(surname) != str:
            raise ValueError("Nazwisko musi być napisem")

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
            raise ValueError("Imię musi być napisem")
        self.name = name

    def set_surname(self, surname: str):
        if not surname or type(surname) is not str:
            raise ValueError("Nazwisko musi być napisem")
        self.surname = surname
    
    def set_pesel(self, Pesel: str):
        if type(Pesel) is int:
            Pesel = str(Pesel)
        if not pesel(Pesel):
            raise ValueError("PESEL musi być poprawny")
        self.pesel = Pesel
        
        