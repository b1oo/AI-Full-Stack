""" Here's an example of a Python program that takes the number of pennies as input and converts it to dollars and cents: """

total_pennies = int(input("Enter the total number of pennies: "))
dollars = total_pennies // 100
cents = total_pennies % 100

print("${0}.{1:02}".format(dollars, cents))