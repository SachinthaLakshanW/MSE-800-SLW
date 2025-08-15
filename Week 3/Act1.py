class Demofile:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            return f.read()

    def write_file(self, text):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(text)

def main():
    Df = Demofile("demo.txt")

    print("Original content:")
    print(Df.read_file())

    Df.write_file("\nNew  line added.")

    print("\nUpdated content:")
    print(Df.read_file())

if __name__ == "__main__":
    main()

