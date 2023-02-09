""" function of a unit converter that changes feet into meters """

def convert_units(value, from_unit, to_unit):
    if from_unit == "feet" and to_unit == "meters":
        return value * 0.3048
    elif from_unit == "meters" and to_unit == "feet":
        return value / 0.3048
    else:
        return "Invalid units"

value = float(input("Enter a value: "))
from_unit = input("Enter the unit to convert from (feet or meters): ")
to_unit = input("Enter the unit to convert to (feet or meters): ")

result = convert_units(value, from_unit, to_unit)
print("Result:", result, to_unit)