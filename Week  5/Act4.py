class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name}, and I live at {self.address}.")

class Student(Person):
    def __init__(self, name, address, age, student_id):
        super().__init__(name, address, age) 
        self.student_id = student_id        

    def greet(self):  # Method overriding
        print(f"Hello, I am {self.name}, a student with ID {self.student_id}.")

# Create a Student object
student1 = Student("Sachintha", "16B Grafton Road, Auckland", 30, "S5588282")

# Call the overridden method
student1.greet()
