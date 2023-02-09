""" pick 6 """

import random

def pick6():
    numbers = []
    for i in range(6):
        numbers.append(random.randint(1, 99))
    return numbers

def num_matches(winning, ticket):
    matches = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            matches += 1
    return matches

def play_pick6(num_plays):
    winning_numbers = pick6()
    expenses = num_plays * 2
    earnings = 0
    for i in range(num_plays):
        ticket = pick6()
        matches = num_matches(winning_numbers, ticket)
        if matches == 1:
            earnings += 4
        elif matches == 2:
            earnings += 7
        elif matches == 3:
            earnings += 100
        elif matches == 4:
            earnings += 50000
        elif matches == 5:
            earnings += 1000000
        elif matches == 6:
            earnings += 25000000
    return earnings - expenses

net_balance = play_pick6(100000)
print("Net balance after playing 100,000 times: $" + str(net_balance))
