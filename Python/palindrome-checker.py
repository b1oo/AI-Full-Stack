""" palindrome checker """

def is_palindrome(word):
    return word == word[::-1]

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if is_palindrome(word1):
    print(f"{word1} is a palindrome.")
else:
    print(f"{word1} is not a palindrome.")

if is_anagram(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")