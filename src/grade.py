class grade:
    def __init__(self, grade: int, scale: int) -> None:
        if(grade > 6):
            raise ValueError("Grade cannot be greater than 6")
        self.grade = grade
        self.scale = scale