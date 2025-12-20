from .staff import Staff

class General(Staff):
    def __init__(self, name: str, age: int, designation: str, department: str):
        super().__init__(name, age, designation)
        self.department = department

    def introduce(self) -> str:
        superclass_intro = super().introduce()
        return f"{superclass_intro} I work in the {self.department} department."