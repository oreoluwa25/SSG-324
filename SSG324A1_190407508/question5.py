result = []
i = 1
while (i <= 100):
    if (i % 2 != 0):
        result.append(i)
    i += 1                                 

print("The odd numbers between 1 and 100 are {}".format(result))