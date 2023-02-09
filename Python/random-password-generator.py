""" random password generator """

import random
import string

def generate_password(length=8): # 8 = length of password
    password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    return password

print(generate_password())
