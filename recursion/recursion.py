def factorial(y):
    if y == 0 or y == 1:
        return (1)
    return y * factorial(y-1)
    
print(factorial(4))

def fib(y):
    if y <= 1:
        return y
    else:
        return fib(y - 1) + fib(y - 2)
    
    
print(fib(7))