class SentenceChecker:
    
    def __init__(self, sentence):
        self.sentence = sentence

    def count_words(self):
        return len(self.sentence.split())
    
def main():
    sentence = input("Hi, Please enter the sentence: ")
    Check = SentenceChecker(sentence)
    
    word_count = Check.count_words()
    print(f"word count in the sentence is: {word_count}")
    
if __name__ == "__main__":
    main()
    
 