""" rot13 example """

def rot13(input_string):
    output_string = ""
    for char in input_string:
        if char.isalpha():
            ascii_value = ord(char)
            if char.islower():
                ascii_value = (ascii_value - 97 + 13) % 26 + 97
            else:
                ascii_value = (ascii_value - 65 + 13) % 26 + 65
            output_string += chr(ascii_value)
        else:
            output_string += char
    return output_string

input_string = input("Enter a string: ")
output_string = rot13(input_string)
print("Encoded string:", output_string)