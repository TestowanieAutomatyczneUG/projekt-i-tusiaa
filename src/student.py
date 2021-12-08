from src.subject import *
from src.Pesel_matcher import pesel

class student:
    def __init__(self, name: str, surname: str, Pesel: str) -> None:
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
        
        