class Person:
    def __init__(self, name, address, age, ID):
        self.name = name
        self.address = address
        self.age = age
        self.ID = ID

    def display_info(self):
        return f"Name: {self.name}, Address: {self.address}, Age: {self.age}, ID: {self.ID}"    

class Student(Person):
    def __init__(self, name, address, age, ID, academic_record):
        super().__init__(name, address, age, ID)
        self.academic_record = academic_record

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Academic Record: {self.academic_record}"  

class Academic(Person):
    def __init__(self, name, address, age, ID, tax_code, salary):
        super().__init__(name, address, age, ID)
        self.tax_code = tax_code
        self.salary = salary

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Tax Code: {self.tax_code}, Salary: {self.salary}"
    
class GeneralStaff(Person):
    def __init__(self, name, address, age, ID, tax_code, pay_rate):
        super().__init__(name, address, age, ID)
        self.tax_code = tax_code
        self.pay_rate = pay_rate

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Tax Code: {self.tax_code}, Pay Rate: {self.pay_rate}" 
    
def main():
    student = Student("Sachintha", "1/3 Queens St", 28, "8448488442", "A+")
    academic = Academic("Dr. Cheif", "Grafton road, Symond st", 36, "A84848484", "TAX12365478", 75000)
    staff = GeneralStaff("Charlie", "5 Yoobee Campus Rd", 35, "G54321", "TX456", 20)

    print(student.display_info())
    print(academic.display_info())
    print(staff.display_info()) 
if __name__ == "__main__":
    main()
    

#The main class Person has common things like name, address, age, and ID.
#Then, other classes (Student, Academic, and Staff) are made from Person. Each one adds its own extra details.
#This way, we don’t have to write the same code again and again. It makes the program shorter and easier to manage.