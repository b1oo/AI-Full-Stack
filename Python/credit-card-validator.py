""" credit card validator """

def is_credit_card_valid(card_number):
    # Convert the input string into a list of ints
    card_number = [int(x) for x in str(card_number)]
    
    # Slice off the last digit (check digit)
    check_digit = card_number[-1]
    card_number = card_number[:-1]
    
    # Reverse the digits
    card_number = card_number[::-1]
    
    # Double every other element in the reversed list
    for i in range(0, len(card_number), 2):
        card_number[i] *= 2
        
    # Subtract nine from numbers over nine
    for i in range(len(card_number)):
        if card_number[i] > 9:
            card_number[i] -= 9
    
    # Sum all values
    total = sum(card_number)
    
    # Take the second digit of the sum
    second_digit = int(str(total)[1])
    
    # If the second digit matches the check digit, the card number is valid
    return second_digit == check_digit