class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
        
class Stack:
    def __init__(self, value):
        newNode = Node(value)
        self.top = newNode
        self.length = 1
    def printstack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
    def gettop(self):
        if self.top is None:
            print("Top: null")
        else:
            print("Top: " + self.top.value)
    def getLength(self):
        print("Length:"+ self.length)
    def makeEmpty(self):
        self.top = None
        self.length = 0
    def push(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
        else: 
            newNode.next = self.top
            self.top = newNode
        self.length += 1
        return self
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.length -= 1
        return self
    