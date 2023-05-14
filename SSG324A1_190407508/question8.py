birthdays = {"Anita": "June 22", "paul": "May 3", "Prom": "July 5"}

name = input("What is your name? ")
if name in birthdays:
    print(birthdays[name], "is the birthday of", name)
else: 
    print("I do not have birthday information for", name)

