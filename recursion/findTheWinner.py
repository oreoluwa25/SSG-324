def findTheWinner(n,m):
    list = []
    start = 0
    for i in range(n):
        list.append(i+1)
    print(list)
    print(len(list))
    
    while len(list) != 1:
        if (m > len(list) and len(list)!=1):
            list.pop()
            
        if list[m-1] == list[len(list)-1]:
            list.pop(list[len(list)-2])
            
        else:
            list.pop(list[m-1])
    return list[0]
        
# wrong

print(findTheWinner(5,2))
        