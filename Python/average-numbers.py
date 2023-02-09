""" average numbers in python """

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0
for number in numbers:
    sum += number

average = sum / len(numbers)
print("The average of the numbers is", average)