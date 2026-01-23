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
            102: 25,
            103: 90,
            104: 38,
            105: 92
        }

    def display_students(self):
        print("Student Details:")
        for student_id in self.students:
            name = self.students[student_id]
            score = self.mse800_scores.get(student_id, "N/A")
            print(f"ID: {student_id}, Name: {name}, MSE800 Score: {score}")

    # PART-2 
    def get_passed_students(self):
        # Merge dictionaries using comprehension conditions
        passed_students = {
            **{student_id: {"name": self.students[student_id], "score": self.mse800_scores[student_id]}
               for student_id in self.students
               if self.mse800_scores.get(student_id, 0) >= 50},
            **{student_id: {"name": self.students[student_id], "score": self.mse800_scores[student_id]}
               for student_id in self.mse800_scores
               if self.mse800_scores.get(student_id, 0) >= 50}
        }
        return passed_students

def main():
    # Create an instance of Student
    student = Student()

    # Display all students
    student.display_students()

    # Display only passed students
    print("\nPassed Students (Score >= 50):")
    passed = student.get_passed_students()
    for student_id, details in passed.items():
        print(f"ID: {student_id}, Name: {details['name']}, MSE800 Score: {details['score']}")


if __name__ == "__main__":
    main()