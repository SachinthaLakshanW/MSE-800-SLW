class Animal:
    def __init__(self, name, age):
        self.name = name   # public attribute
        self._type = "Domestic Animal"     # protected attribute
        self.__age = age  # private attribute

    def show_age(self):    # method using private attribute
        print(f"Our {self.name}'s age is {self.__age} years.")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def show_info(self):
        # # method using Public and Protected attribute.
        print(f"Our Other Pet is a Dog. Her name is {self.name}. She is {self.breed} and lovely {self._type} to have around.")

def main():
    a = Animal("Cat", 5)
    a.show_age()

    d = Dog("Princy", 12, "Crossbreed")
    d.show_info()

if __name__ == "__main__":
    main()


