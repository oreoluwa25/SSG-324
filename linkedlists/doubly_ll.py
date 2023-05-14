class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class DoublyLinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
        
    def printList(self):
        node = self.head
        listStr = ''
        while node:
            if node.next is None:
                listStr+=str(node.data)
            else:
                listStr+=str(node.data)+'->'
            node = node.next
        print(listStr)
        return self
    
    #push - O(1)
    def addToTheEnd(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        self.length+=1
        return self
    #this works also, but it has higher complexity - O(n)
        # temp = self.head
        # while temp and temp.next:
        #     temp = temp.next
        # temp.next = newNode
        # newNode.prev = temp
        # self.tail = newNode
        # self.length+=1
        # return self
    
    #pop - O(1)
    def removeFromTheEnd(self):
        if self.head is None:
            print('empty list')
            return
        self.tail = self.tail.prev
        self.tail.next = None
        self.length-=1
        return self
        
    #shift - O(1)
    def removeFromTheBeginning(self):
        if self.head is None:
            print('empty list')
            return
        temp = self.head
        self.head = temp.next
        temp.next = temp.next.next
        self.length-=1
        return self
    
    #unshift - O(1)
    def addToTheBeginning(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.length+=1
        return self
    
    #get - O(n)
    def getAtIndex(self,index):
        if self.head is None:
            print('empty list')
            return
        if index >= self.length or index < 0:
            print('index out of bounds')
            return
        temp = self.head
        count = 0
        while temp:
            if count == index:
                return temp
            else:
                count+=1
            temp = temp.next
        return temp
    
    #set - O(1)
    def setAtIndex(self,index, value):
        newNode = Node(value)
        node = self.getAtIndex(index)
        if node is None:
            return
        newNode.next = node.next
        newNode.prev = node.prev
        node.data = newNode.data
        return self
    
    #insert
    def insertAtIndex(self, index, value):
        newNode = Node(value)
        node = self.getAtIndex(index - 1)
        temp = node.next
        newNode.next = temp
        node.next = newNode
        newNode.prev = temp.prev
        
        self.length+=1
        return self
    
    #remove
    def removeAtIndex(self,index):
        node = self.getAtIndex(index - 1)
        if index == 0:
            self.removeFromTheBeginning()
            return
        if index == self.length-1:
            self.removeFromTheEnd()
            return
        print(node.data)
        node.next = node.next.next
        self.length-=1
        return self
    
    #reverse
    def reverseList(self):
        if self.head is None:
            return
        curr = self.head
        self.head = self.tail
        self.tail = curr
        prev = None
        next = curr.next
        for i in range(self.length):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return self
            

        
        
        
        
    
myDoublyList = DoublyLinkedList(9)
myDoublyList.addToTheEnd(4)
myDoublyList.addToTheEnd(8)
myDoublyList.addToTheEnd(16)
myDoublyList.addToTheBeginning(6)
myDoublyList.addToTheBeginning(2)
myDoublyList.removeFromTheEnd()
myDoublyList.removeFromTheEnd()
myDoublyList.removeFromTheBeginning()
myDoublyList.removeFromTheBeginning()
myDoublyList.getAtIndex(5)
myDoublyList.setAtIndex(1,5)
myDoublyList.addToTheEnd(6)
myDoublyList.insertAtIndex(1,6)
myDoublyList.insertAtIndex(2,8)
myDoublyList.removeAtIndex(2)
myDoublyList.reverseList()
myDoublyList.printList()