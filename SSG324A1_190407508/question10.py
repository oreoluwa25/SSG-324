def maximum(a, b, c):
    max = 0
    
    if(a >= b) and (a >= c):
        max = a
    elif (b >= a) and (b >= c):
        max = b
    else: 
        max = c
    print("Maximum number of the three provided numbers is", max)

a = int(input("Please input a number: "))
b = int(input("Please input another number: "))
c = int(input("Please input another number: "))

maximum(a,b,c)