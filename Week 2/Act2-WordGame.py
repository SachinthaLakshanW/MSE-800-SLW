import random

class TestWordGame:
    def __init__(self):
        self.words = ["food", "table", "auckland", "new zealand", "laptop", "word", "please"]
        self.word = random.choice(self.words)
        self.blanks = ["_" if c != " " else " " for c in self.word]
        self.attempts = 10
        self.guessed_letters = set()

    def Gameon(self):
        while self.attempts > 0 and "_" in self.blanks:
            print("Word:", " ".join(self.blanks))
            print("Attempts left:", self.attempts)
            guess = input("Guess a letter: ").lower()

            if not guess.isalpha() or len(guess) != 1:
                print("Type only one letter.")
                continue
            self.guessed_letters.add(guess)

            if guess in self.word:
                for i, c in enumerate(self.word):
                    if c == guess:
                        self.blanks[i] = guess
                print("Yes!")
            else:
                self.attempts -= 1
                print("Nope!")

        if "_" not in self.blanks:
            print("You win! The word was:", self.word)
        else:
            print("You lose! The word was:", self.word)

if __name__ == "__main__":
    game = TestWordGame()
    game.Gameon()
