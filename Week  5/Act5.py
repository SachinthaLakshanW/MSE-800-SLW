class Color:
    def __init__(self, color_name):
        self.color_name = color_name

    def show_color(self):
        return f"Color: {self.color_name}"

class TransparentColor(Color): 
    def __init__(self, color_name, transparency):
        super().__init__(color_name)
        self.transparency = transparency

    def show_color(self):
        return f"Color: {self.color_name}, Transparency: {self.transparency}%"

class Animal:
    def __init__(self, name, color: Color):
        self.name = name
        self.color = color

    def describe(self):
        return f"Animal: {self.name}, {self.color.show_color()}"

def main():
    lion = Animal("Lion", Color("Golden"))
    print(lion.describe())

    jellyfish = Animal("Jellyfish", TransparentColor("Blue", 70))
    print(jellyfish.describe())

if __name__ == "__main__":
    main()