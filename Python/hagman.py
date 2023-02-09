# In this example, the play_hangman function takes a word as an input and implements the game of Hangman. The word is displayed to the player as a series of underscores, with correctly guessed letters being filled in. The player is prompted to guess a letter, and if the letter is in the word, it is filled in. If the letter is not in the word, the number of tries decreases. The game continues until the player either correctly guesses all the letters in the word or runs out of tries.
import random

def display_word(word, letters_guessed):
    display = []
    for letter in word:
        if letter in letters_guessed:
            display.append(letter)
        else:
            display.append("_")
    return " ".join(display)

def get_guess(letters_guessed):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
        elif guess in letters_guessed:
            print("You already guessed that letter. Please try again.")
        elif not guess.isalpha():
            print("Invalid input. Please enter a letter.")
        else:
            return guess

def play_hangman(word):
    word = word.lower()
    letters_guessed = []
    tries = 6
    print("Welcome to Hangman!\n")
    while tries > 0:
        print("Current word:", display_word(word, letters_guessed))
        print("Tries remaining:", tries)
        guess = get_guess(letters_guessed)
        letters_guessed.append(guess)
        if guess in word:
            print("Correct!")
            if "_" not in display_word(word, letters_guessed):
                print("You won! The word was", word + ".")
                return
        else:
            print("Incorrect.")
            tries -= 1
    print("You lost! The word was", word + ".")

# Choose a random word from a list of words
words = ["python", "java", "javascript", "csharp", "swift"]
word = random.choice(words)

play_hangman(word)