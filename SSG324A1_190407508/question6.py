grade = int(input("What is your grade in percentage? "))

if grade > 90:
    print("You have an A")
elif 80 < grade <= 90:
    print("You have a B")
elif 60 <= grade <= 80:
    print("You have a C")
else:
    print("You have a D")