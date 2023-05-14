# ordered collection of items
# stores items in key/value pairs
# e.g
capital_city = {'Paris': 'Rom', 'England': 'London', }
print(capital_city)
capital_city['Japan'] = 'Tokyo'
print(capital_city)
# the key cannot change but the value can - immutable
capital_city['Paris'] = 'Rome'
print(capital_city)
print(capital_city['England'])

del capital_city['Japan']
print(capital_city)

# if a key does not exist, you get a keyerror
# print(capital_city['USA'])

squares = {1:1, 2:4, 3:9, 4:16, 5:25, 7:49}
print(1 in squares)
print(8 in squares)
print(9 not in squares)

for i in squares:
    print(i)


