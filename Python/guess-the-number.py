""" guess the number """

import random

random_number = random.randint(1, 10)

while True:
    print("Guess a number between 1 and 10:")
    guess = int(input())

    if guess == random_number:
        print("You won! The number was", random_number)
        break
    elif guess < random_number:
        print("Too low.")
    else:
        print("Too high.")