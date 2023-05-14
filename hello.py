def func():
    print('hey')
    
def positiveInt():
    num = int(input('Enter a number:'))
    if num < 0:
        num = 0
        print('negative changed to zero')
    elif num == 0:
        print('zero')
    elif num == 1:
        print('single')
    else:
        print('more')
def sumOfThree():
    x = int(input('Please input the first number:'))
    y = int(input('Please input the second number:'))
    z = int(input('Please input the third number:'))
    sum = x+y+z
    print('the sum of', x, y,'and', z, 'is', sum)
    
def f(x):
    return x*x

def fib(num):
    a,b = 0,1
    while b < num:
        print(b)
        a,b = b,a+b
        
def forLoop():
    words = ['hey', 'whats up', 'bye']
    for word in words:
        print(word, len(word))
    
def rangeStatement():
    for num in range(3,13,2):
        print('ore')
        
def tryingBreak():
    for x in range(4,14):
        for n in range(4,x):
            if x % n == 0:
                print(x,'equals',n,'*',x//n)
                continue
    else:
        print('has a remainder of', x%n)

def find20AndUpdate():
    listToReplace = [5,20,15,20,25,50,20]
    for n in range(len(listToReplace)):
        if listToReplace[n] == 20:
            listToReplace[n] = 200
            break
    print(listToReplace)
    
def remove20():
    listToRemove20 = [5,20,15,20,25,50,20]
    for num in listToRemove20:
        if num == 20:
            listToRemove20.remove(num)
            continue
    print(listToRemove20)
        
    
def addListNumbers():
    listToAdd = [5,20,15,20,25,50,20]
    sum = 0
    for num in listToAdd:
        sum = sum + num
    print(sum)
    
def squareOfElements():
    list = []
    for i in range(1,31):
        list.append(i*i)
    newListOne = list[:5]
    newListTwo = list[-5:]
    newList = newListOne + newListTwo
    print(newList)
    
    
    
def confirm(prompt, retries=3, reminder='try again in 30 seconds'):
    while True:
        okay = input(prompt)
        if okay in ('y', 'ye', 'yes'):
            return True
        if okay in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid input')
        print(reminder)
        
def hyphenTenate(*args, sep='-'):
    print(sep.join(args))
    
def makeDecrementor(n):
    return lambda x:n-x

def main():
    print(5*'Yes')
    print('my name', 'is', 'ore')
    print('my name', 'is', 'ore', sep='-')
    silly = '''Say "I'm in"
    This is another line'''
    print(silly)
    func()
    squares = [1,4,9,16,25]
    print(squares[-4:])
    squares.append(36)
    letters = ['a', 'b', 'c', 'd', 'e']
    letters[2:4] = ['C']
    print(letters)
    cubes = [1,8,27,65,125]
    cubes[3] = 64
    print(cubes)
    print(cubes+squares)
    positiveInt()
    print(len([3,5,9]))
    print(list())
    print(2*3)
    print(23%3)
    print(23/3)
    print(23//3)
    print(2+3)
    print(str(23))
    print(int('123'))
    print(max(2,11,55))
    sumOfThree()
    print(f(3)+f(4))
    print(16+f(4))
    fib(25)
    forLoop()
    rangeStatement()
    tryingBreak()
    find20AndUpdate()
    remove20()
    addListNumbers()
    squareOfElements()
    hyphenTenate('what', 'do', 'you', 'mean')
    confirm('do you really want to quit?')
    decrement = makeDecrementor(100)
    print(decrement(2))
main()
