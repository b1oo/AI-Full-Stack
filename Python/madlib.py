""" In this example, the madlib function takes a verb, adjective, and noun as inputs and returns a sentence with the inputs filled in. The get_word function prompts the user to enter a word, and the madlib function uses the words entered by the user to create a sentence. The sentence is then displayed to the user.
"""
def get_word(prompt):
    return input(prompt)

def madlib(verb, adjective, noun):
    return "Do you %s your %s %s?" % (verb, adjective, noun)

print("Welcome to the Mad Lib game!")
verb = get_word("Enter a verb: ")
adjective = get_word("Enter an adjective: ")
noun = get_word("Enter a noun: ")

print(madlib(verb, adjective, noun))