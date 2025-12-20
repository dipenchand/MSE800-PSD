from .staff import Staff

class Academic(Staff):
    def __init__(self, name: str, age: int, designation: str, publication: str):
        super().__init__(name, age, designation)
        self.publication = publication

    def introduce(self) -> str:
        superclass_intro = super().introduce()
        return f"{superclass_intro} I've published {self.publication}."