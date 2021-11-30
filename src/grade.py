class grade:
    def __init__(self, grade: int, scale: int) -> None:
        if(grade > 6):
            raise ValueError("Grade cannot be greater than 6")
        if(grade < 1):
            raise ValueError("Grade cannot be less than 1")
        if(scale > 10):
            raise ValueError("Scale cannot be greater than 10")
        self.grade = grade
        self.scale = scale