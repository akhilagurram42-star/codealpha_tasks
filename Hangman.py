import random

words = ["apple", "mango", "grape"]
word = random.choice(words)

guessed = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("Word:", display)

    guess = input("Enter a letter: ").lower()

    if guess in word:
        guessed.append(guess)
    else:
        attempts -= 1
        print("Attempts left:", attempts)

    if all(l in guessed for l in word):
        print("You won! Word:", word)
        break

if attempts == 0:
    print("You lost! Word:", word)