""" vocabulary frequency """

import string

def analyze_book(file_path):
    # create an empty dictionary to store the word count
    word_count = {}

    # open the file
    with open(file_path, 'r', encoding='utf-8') as file:
        # read the content of the file
        content = file.read()

        # make everything lowercase
        content = content.lower()

        # remove punctuation
        content = content.translate(str.maketrans("", "", string.punctuation))

        # split the content into a list of words
        words = content.split()

        # loop through the words
        for word in words:
            # check if the word is already in the dictionary
            if word in word_count:
                # if it is, increment its count
                word_count[word] += 1
            else:
                # if it isn't, add it with a count of 1
                word_count[word] = 1

    # sort the dictionary based on the count in descending order
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # print the top 10 frequent words
    print("The top 10 frequent words are:")
    for i in range(10):
        print(f"{sorted_word_count[i][0]}: {sorted_word_count[i][1]}")
