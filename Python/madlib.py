"""In this example, the get_word function is used to prompt the user to enter a word, which is then stored in a variable. The Mad Lib is created using string concatenation to combine the words entered by the user into a sentence, which is then stored in the mad_lib variable. Finally, the Mad Lib is printed to the screen."""

def get_word(prompt):
    return input(prompt)

verb = get_word("Enter a verb: ")
adjective = get_word("Enter an adjective: ")
noun = get_word("Enter a noun: ")

mad_lib = "Do you " + verb + " your " + adjective + " " + noun + "?"

print(mad_lib)