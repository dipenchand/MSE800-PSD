from .person import Person

class Staff(Person):
    def __init__(self, name: str, age: int, designation: str):
        super().__init__(name, age)
        self.designation = designation
        
    def introduce(self) -> str:
        superclass_intro = super().introduce()
        return f"{superclass_intro} I work as a {self.designation}."