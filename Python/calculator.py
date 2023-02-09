""" calculator in python using REPL """

while True:
    print("Enter operator: (+, -, *, /)")
    operator = input()
    
    if operator in ('+', '-', '*', '/'):
        break
    else:
        print("Invalid operator! Please try again.")

print("Enter first operand:")
first_operand = float(input())

print("Enter second operand:")
second_operand = float(input())

if operator == '+':
    result = first_operand + second_operand
elif operator == '-':
    result = first_operand - second_operand
elif operator == '*':
    result = first_operand * second_operand
else:
    result = first_operand / second_operand

print("Result:", result)