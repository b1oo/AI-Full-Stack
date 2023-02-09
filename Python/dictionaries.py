""" practicel example of a dictionary being used in python """

# Creating a dictionary
person = {
    "name": "John Doe",
    "age": 32,
    "email": "johndoe@example.com"
}

# Accessing values in a dictionary
print("Name:", person["name"])
print("Age:", person["age"])
print("Email:", person["email"])

# Updating values in a dictionary
person["age"] = 33
print("Age:", person["age"])

# Adding a new key-value pair to a dictionary
person["address"] = "123 Main St"
print("Address:", person["address"])

# Removing a key-value pair from a dictionary
del person["email"]
print("Email:", person.get("email", "Not found"))