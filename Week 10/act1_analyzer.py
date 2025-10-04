##Activity 1 - Analyzer: Calculates length and uppercase letters for strings or lists.##
class Analyzer:
    def __init__(self, data):
        self.data = data

    def total_length(self):
        return len(self.data)

    def uppercase_count(self):
        items = self.data if isinstance(self.data, list) else list(self.data)
        return sum(1 for x in items if isinstance(x, str) and x.isupper())


def main():
    text = "Sky Beyond Borders"
    words = ["AI", "Sky", "NZ"]

    a1 = Analyzer(text)
    print("Text:", text)
    print("Length:", a1.total_length())
    print("Uppercase:", a1.uppercase_count())

    a2 = Analyzer(words)
    print("\nList:", words)
    print("Length:", a2.total_length())
    print("Uppercase:", a2.uppercase_count())


if __name__ == "__main__":
    main()
