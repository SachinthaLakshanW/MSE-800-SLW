class Staff:
    def __init__(self, full_name, pay, position):
        self.full_name = full_name
        self.pay = pay
        self.position = position

    def display_info(self):
        print("Full Name:", self.full_name)
        print("Pay:", f"${self.pay}")
        print("Position:", self.position)

    def give_raise(self, bonus_amount):
        self.pay += bonus_amount
        print(f"New Pay for {self.full_name}: ${self.pay}")

def run():
    s1 = Staff("Sachintha", 48000, "HR Executive")
    s2 = Staff("Lakshan", 60000, "Project Manager")

    print("Staff Member 1:")
    s1.display_info()
    s1.give_raise(3000)

    print("\nStaff Member 2:")
    s2.display_info()
    s2.give_raise(4500)

if __name__ == "__main__":
    run()


