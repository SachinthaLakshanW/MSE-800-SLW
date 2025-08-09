class StringManipulator:
    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text.find(char)
    
    def find_length(self):
        return len(self.text)   
    
    def to_uppercase(self):
        return self.text.upper()

# create an instance of the StringManipulator class
name = StringManipulator("Example")

# Call the methods
char_index = name.find_character('x')
length = name.find_length()
upper_text = name.to_uppercase()

print("Index of 'x':", char_index)
print("Length:", length)
print("Text in uppercase:", upper_text)
