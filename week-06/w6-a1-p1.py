class Student:
    def __init__(self):
        # Dictionary: student_id -> student_name
        self.students = {
            101: "Bhaskar",
            102: "Sushil",
            103: "Saksham",
            104: "Divya",
            105: "Sushil"
        }

        # Dictionary: student_id -> MSE800 score
        self.mse800_scores = {
            101: 78,
            102: 85,
            103: 90,
            104: 88,
            105: 92
        }

    def display_students(self):
        print("Student Details:")
        for student_id in self.students:
            name = self.students[student_id]
            score = self.mse800_scores.get(student_id, "N/A")
            print(f"ID: {student_id}, Name: {name}, MSE800 Score: {score}")

# Create an instance of Student
student = Student()

# Display all students
student.display_students()