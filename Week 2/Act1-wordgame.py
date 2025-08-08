import random

def main():
    words = ["food", "table", "auckland", "new zealand", "laptop", "word", "please"]
    word = random.choice(words)
    blanks = ["_" if c != " " else " " for c in word]
    attempts = 10
    guessed_Letters = set()

    while attempts > 0 and "_" in blanks:
        print("Word:", " ".join(blanks))
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Type only one letter.")
            continue

        guessed_Letters.add(guess)

        if guess in word:
            for i, c in enumerate(word):
                if c == guess:
                    blanks[i] = guess
            print("Yes!")
        else:
            attempts -= 1
            print("Nope!")

    if "_" not in blanks:
        print("You win! The word was:", word)
    else:
        print("You lose! The word was:", word)

if __name__ == "__main__":
    main()
