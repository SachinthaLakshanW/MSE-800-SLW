
class StringManipulator:
    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text(char)
    
    def find_length(self):
        return len(self.text)   
    #create an instance of the StringManipulator class
    
name = StringManipulator("Example")

    
    #Call the find_character method on the object
result = name.find_character('x')
result = name.find_length()
print(result)

        