# Base class
class Color:
    def __init__(self, color):
        self.color = color

    def show(self):
        return f"{self.color}"

# Child class adds transparency and pattern
class TransparentColor(Color):
    def __init__(self, color, transparency, pattern="plain"):
        super().__init__(color)
        self.transparency = transparency
        self.pattern = pattern

    def show(self):
        return f"{self.color} ({self.pattern}) with {self.transparency}% transparency"

# Animal class uses TransparentColor
class Animal(TransparentColor):
    def __init__(self, name, color, transparency, pattern="plain"):
        super().__init__(color, transparency, pattern)
        self.name = name

    def describe(self):
        return f"{self.name} looks {self.show()}"

# Main function
def main():
    zebra = Animal("Zebra", "Black & White", 50, "striped")
    parrot = Animal("Parrot", "Green", 30, "spotted")

    print(zebra.describe())
    print(parrot.describe())

if __name__ == "__main__":
    main()
