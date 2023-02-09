""" rock paper scissors """

import random

def play_game():
    print("Rock, Paper, Scissors Game")
    print("=========================")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    player = int(input("Enter your choice (1-3): "))
    computer = random.randint(1, 3)

    if player == computer:
        print("Draw")
    elif player == 1 and computer == 2:
        print("Computer wins")
    elif player == 1 and computer == 3:
        print("Player wins")
    elif player == 2 and computer == 1:
        print("Player wins")
    elif player == 2 and computer == 3:
        print("Computer wins")
    elif player == 3 and computer == 1:
        print("Computer wins")
    elif player == 3 and computer == 2:
        print("Player wins")
    else:
        print("Invalid choice")

play_game()