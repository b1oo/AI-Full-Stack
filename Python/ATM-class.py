"""Here's an example of an ATM class in Python """

class ATM:
    def __init__(self, balance=0, interest_rate=0.001):
        self.balance = balance
        self.interest_rate = interest_rate
        
    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        
    def check_interest_rate(self):
        return self.interest_rate
    
    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
