class grade:
    def __init__(self, grade: int, scale: int) -> None:
        if type(grade) is not int:
            raise ValueError("Grade must be an integer")
        if type(scale) is not int:
            raise ValueError("Scale must be an integer")
        if(grade > 6):
            raise ValueError("Grade cannot be greater than 6")
        if(grade < 1):
            raise ValueError("Grade cannot be less than 1")
        if(scale > 10):
            raise ValueError("Scale cannot be greater than 10")
        if(scale < 1):
            raise ValueError("Scale cannot be less than 1")
        self.grade = grade
        self.scale = scale

    def get_grade(self) -> int:
        return self.grade

    def get_scale(self) -> int:
        return self.scale