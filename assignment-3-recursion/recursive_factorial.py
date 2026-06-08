def recursive_factorial (n):
#Base case: factorial of 0 or 1 is 1
    if n <=1:
        return 1
    # Recursive call: the function calls itself with (n-1)
    return n * recursive_factorial(n-1)

print (recursive_factorial(5))