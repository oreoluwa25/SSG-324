def factorial(x):
    if x == 0 or x ==1:
        return (1)
    return x * factorial(x - 1)

print(factorial(4))

def get_fib(position):
    if position <= 1:
        return position
    else:
        return get_fib(position - 1) + get_fib(position - 2)

print(get_fib(9))