# In this example, the fibonacci function takes an integer n as an input and calculates the nth number in the Fibonacci sequence using a recursive approach. The base case is defined as if n <= 1, in which case the function returns n. In all other cases, the function returns fibonacci(n-1) + fibonacci(n-2), which means it calls itself twice with n-1 and n-2 as arguments. This allows the function to keep calling itself until the base case is reached, at which point the function returns the value of n. The result of each call is then added together to give us the final result.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Output: 55