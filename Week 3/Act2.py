class Demofile:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            return f.read()

    def count_words(self):
        content = self.read_file()
        words = content.split()
        return len(words)   
    
def main():
    Df = Demofile("demo.txt")

    print("Original content:")
    print(Df.read_file())

    word_count = Df.count_words()
    print(f"\nTotal number of words: {word_count}")

if __name__ == "__main__":
    main()