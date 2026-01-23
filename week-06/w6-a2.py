import sqlite3

class Student:
    def __init__(self, db_name="students.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.init_database()
    
    def init_database(self):
        # Initialize database connection and create table
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        
        # Create table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Student (
                student_id INTEGER PRIMARY KEY,
                student_name TEXT NOT NULL,
                score INTEGER NOT NULL
            )
        ''')
        self.conn.commit()
        
        # Insert sample data
        self.insert_sample_data()
    
    def insert_sample_data(self):
        # Insert sample student data into the database
        sample_data = [
            (101, "Bhaskar", 78),
            (102, "Sushil", 25),
            (103, "Saksham", 90),
            (104, "Divya", 38),
            (105, "Sushil", 92)
        ]
        
        # Clean existing data first
        self.cursor.execute('DELETE FROM Student')
        
        # Insert new data
        self.cursor.executemany(
            'INSERT INTO Student (student_id, student_name, score) VALUES (?, ?, ?)',
            sample_data
        )

        self.conn.commit()

    # All students 
    def display_students(self):
        # Display all students from database
        print("Student Details:")
        self.cursor.execute('SELECT student_id, student_name, score FROM Student')
        students = self.cursor.fetchall()
        for student_id, name, score in students:
            print(f"ID: {student_id}, Name: {name}, MSE800 Score: {score}")

    # PART-2: Only passed students
    def get_passed_students(self):
        # Get students who passed with score >= 50 from database
        self.cursor.execute('''
            SELECT student_id, student_name, score FROM Student 
            WHERE score >= 50
        ''')
        return self.cursor.fetchall()
        # students = self.cursor.fetchall()
        # passed_students = {
        #     student_id: {"name": name, "score": score}
        #     for student_id, name, score in students
        # }
        # return passed_students
    
    # A2: Only Top 3 students
    def get_top_students(self, limit=3):
        # Retrieve top students by score from database by sorting descending
        self.cursor.execute('''
            SELECT student_id, student_name, score FROM Student 
            ORDER BY score DESC 
            LIMIT ?
        ''', (limit,))
        return self.cursor.fetchall()
    
    def close_database(self):
        # Close database connection
        if self.conn:
            self.conn.close()

def main():
    # Create an instance of Student
    student = Student()

    # Display all students
    student.display_students()

    # Display only passed students
    print("\nPassed Students (Score >= 50):")
    passed = student.get_passed_students()
    for student_id, name, score in passed:
        print(f"ID: {student_id}, Name: {name}, MSE800 Score: {score}")

    # Display top 3 students
    print("\nTop 3 Students by Score:")
    top_students = student.get_top_students(3)
    for i, (student_id, name, score) in enumerate(top_students, start=1):
        print(f"RANK: {i} ID: {student_id}, Name: {name}, MSE800 Score: {score}")

    # Close database connection
    student.close_database()


if __name__ == "__main__":
    main()