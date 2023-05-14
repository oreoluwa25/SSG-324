a = int(input("What is the first number? "))
b = int(input("What is the second number? "))


def sum(a, b):
    sum = a + b
    if 15 <= sum <= 20:
        return 20
    else:
        return sum

print(sum(a, b))

