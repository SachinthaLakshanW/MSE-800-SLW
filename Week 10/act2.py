"""Activity 2 - Analyzer: counts length, uppercase, digits, special chars."""

class Analyzer:
    """Analyze text or list for length, uppercase, digits, and special chars."""
    def __init__(self, data):
        self.data = data

    def total_length(self):
        return len(self.data)

    def uppercase_count(self):
        return sum(1 for x in (self.data if isinstance(self.data, list) else list(self.data))
                   if isinstance(x, str) and x.isupper())

    def digit_count(self):
        return sum(1 for x in (self.data if isinstance(self.data, list) else list(self.data))
                   if isinstance(x, str) and x.isdigit())

    def special_count(self):
        return sum(1 for x in (self.data if isinstance(self.data, list) else list(self.data))
                   if isinstance(x, str) and not x.isalnum())


def main():
    """Run simple tests of the Analyzer class."""
    text = "Sky123!@#"
    words = ["AI", "Sky99", "NZ!"]

    a1 = Analyzer(text)
    print("Text:", text, "Length:", a1.total_length(), "Uppercase:", a1.uppercase_count(),
          "Digits:", a1.digit_count(), "Special:", a1.special_count())

    a2 = Analyzer(words)
    print("List:", words, "Length:", a2.total_length(), "Uppercase:", a2.uppercase_count(),
          "Digits:", a2.digit_count(), "Special:", a2.special_count())


if __name__ == "__main__":
    main()
