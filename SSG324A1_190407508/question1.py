numbers = []
for i in range(1500, 2701):
    if (i % 7 == 0) and (i % 5 == 0):
        numbers.append(i)

print("The numbers divisible by 7 and mulitiples of 5 between 1500 and 2701 are {}".format(numbers))