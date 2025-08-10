class HumanResourceSystem :
    def __init__(self):
        self.personal_details = []

    def collect_details(self):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        address = input("Enter your address: ")
        self.personal_details = [name, age, address]

    def display_details(self):
        print(f"Name: {self.personal_details[0]}")
        print(f"Age: {self.personal_details[1]}")
        print(f"Address: {self.personal_details[2]}")
        print("Thank you for providing your details.")

    def update_age(self):
        years_to_add = int(input("Please add the no of years you need to add to the age? "))
        current_age = int(self.personal_details[1])
        new_age = current_age + years_to_add
        self.personal_details[1] = str(new_age)
        print(f"Updated Age: {self.personal_details[1]}")
    def display_updated_info(self):
        print(f"Updated Information: Name: {self.personal_details[0]}, Age: {self.personal_details[1]}, Address: {self.personal_details[2]}")
def main():
    hr_system = HumanResourceSystem()
    hr_system.collect_details()
    hr_system.display_details()
    hr_system.update_age()
    hr_system.display_updated_info()
if __name__ == "__main__":
    main()