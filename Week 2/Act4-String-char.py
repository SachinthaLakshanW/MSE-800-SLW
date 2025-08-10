class StringManipulator:
  
    def find_character(text, char):
        return text.find(char)

    def get_length(text):
        return len(text)

    def to_uppercase(text):
        return text.upper()

def main():
    text = "example"

    print("Index of 'x':", StringManipulator.find_character(text, 'x'))
    print("Length of string:", StringManipulator.get_length(text))
    print("Uppercase string:", StringManipulator.to_uppercase(text))


if __name__ == "__main__":
    main()

#The __init__ method stores the string in the object when it's created, so we don’t need to pass it to each method. This makes the code shorter and easier to use.