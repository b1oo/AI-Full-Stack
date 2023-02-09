""" type script then print print(number_to_words(67)) # outputs "sixty-seven"
"""

def number_to_words(number):
    if number < 0 or number > 99:
        return "Invalid input. Please enter a number between 0 and 99."
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if number < 20:
        return ones[number]
    else:
        return tens[number // 10] + (ones[number % 10] if number % 10 != 0 else "")
