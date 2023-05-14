week = {1:"Monday", 2:"Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

day = int(input("Input a number between 1 and 7: "))

if day in week:
    print("The day is", week[day])
else:
    print("Invalid Number")