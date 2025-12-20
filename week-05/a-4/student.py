from .person import Person

class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id
    
    def introduce(self) -> str:
        # Calling the introduce method from the Person class
        superclass_intro = super().introduce()
        return f"{superclass_intro} My student ID is {self.student_id}."