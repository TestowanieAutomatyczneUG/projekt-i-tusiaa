from src.subject import *

class student:
    def __init__(self, name: str, surname: str, pesel: int) -> None:
        self.subjects = []
        self.remarks = []
        self.name = name
        self.surname = surname
        self.pesel = pesel
        