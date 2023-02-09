""" In this example, a list of possible responses for the Magic 8 Ball is created and stored in the responses variable. The magic_8_ball function uses the random.choice function from the random module to randomly choose one of the responses and return it. Finally, the returned response is printed to the screen. """

import random

responses = [    "It is certain",    "It is decidedly so",    "Without a doubt",    "Yes, definitely",    "You may rely on it",    "As I see it, yes",    "Most likely",    "Outlook good",    "Yes",    "Signs point to yes",    "Reply hazy try again",    "Ask again later",    "Better not tell you now",    "Cannot predict now",    "Concentrate and ask again",    "Don't count on it",    "My reply is no",    "My sources say no",    "Outlook not so good",    "Very doubtful"]

def magic_8_ball():
    return random.choice(responses)

print(magic_8_ball())