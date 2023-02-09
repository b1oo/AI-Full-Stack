""" emoji generator """

import random

emoticons = [":)", ";)", ":(", ":D", ":'(", ":P", ";P", ":O", "B)", ":@"]

def random_emoticon():
    return random.choice(emoticons)

print(random_emoticon())