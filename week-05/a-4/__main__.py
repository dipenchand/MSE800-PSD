# Importing Person and Student classes
from .person import Person
from .student import Student
from .staff import Staff
from .general import General
from .academic import Academic

def main():
    # Creating Person object
    person = Person("Alice", 30)
    # Accessing person method
    print("***** Executing Person class *****")
    print(person.introduce())
    print("\n")
    
    # Creating Student object and passing ID as an additional attribute
    student = Student("Bob", 20, "S12345")
    print("***** Executing Student class *****")
    print(student.introduce())
    
    # Creating Staff object and passing Designation as an additional attribute
    staff = Staff("John", 30, "Engineer")
    print("\n***** Executing Staff class *****")
    print(staff.introduce())
    
    # Creating General object and passing additional attribute
    general = General(staff.name, staff.age, staff.designation, "IT")
    print("\n***** Executing General class *****")
    print(general.introduce())
    
    # Creating Academic object and passing additional attribute
    general = Academic(general.name, general.age, general.designation, "Advanced Computing")
    print("\n***** Executing General class *****")
    print(general.introduce())

if __name__ == "__main__":
    main()