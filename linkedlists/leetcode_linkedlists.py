class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
        
    def printList(self):
        curr = self.head
        list = ''
        while curr:
            if curr.next is None:
                list+= str(curr.data)
            else:
                list+= str(curr.data) + '->'
            curr = curr.next
        print(list)
        
    def printListLength(self):
        print(self.length)
        return
        
    
    def addToTheBeginning(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return self
        temp = self.head
        newNode.next = temp
        self.head = newNode
        self.length += 1
        return self
    
    def addToTheEnd(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.length+=1
            return
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        curr.next = newNode
        newNode.next = None
        self.length+=1    
        return self    
        
        
        
    def getAtIndex(self, index):
        if(self.length <= index or index < 0):
            print("index out of bounds")
            return
        temp = self.head
        for i in range (index):
            temp = temp.next
        return temp
    
    
    def getAtIndexFromTheEnd(self, index):
        if(self.length <= index or index < 0):
            print("index out of bounds")
            return
        counter = self.length - 1
        temp = self.head
        for i in range (index):
            counter-=1
            
        for j in range(counter):
            temp = temp.next
        print(temp.data)
        return temp
    
    def setAtIndex(self, index, newValue):
        newNode = Node(newValue)
        oldValue = self.getAtIndex(index)
        newNode.next = oldValue.next
        oldValue.data = newNode.data
        return newNode
    
    
    #1 - Remove Nth Node From End of List
    def removeAtIndexFromTheEnd(self, index):
        node = self.getAtIndexFromTheEnd(index)
        if node is None:
            return
        temp = node.next
        prev = self.head
        while prev:
            if prev.next == node:
                prev.next = temp
            prev = prev.next
        return self
    
    #2
    # def mergeTwoLists(list1, list2):
    #     mergedList = LinkedList
    #     pointer = mergedList
        
    #     while list1 and list2:
    #         if list1.data <= list2.data:
    #             pointer.next = list1
    #             list1 = list1.next
    #         else:
    #             pointer.next = list2
    #             list2 = list2.next
                
    #     print(mergedList)
    #3 - remove and leave only one
    def removeDuplicates(self):
        if self.head is None:
            print('empty list')
            return
        curr = self.head
        while curr and curr.next:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
                self.length-=1
            else:
                curr = curr.next
        return self
    #3 - delete completely
    def deleteDuplicates(self):
        if self.head is None:
            print('no items in the list')
            return
        curr = self.head
        prev = curr
        while curr:
            if curr.next and curr.next.data == curr.data:
                while curr.next and curr.next.data == curr.data:
                    curr = curr.next
                    prev.next = curr.next
                    self.length-=1
            else:
                prev = prev.next
            curr = curr.next
        return self
    
    #4 - remove an element, no matter how many times it shows up
    def removeElement(self, value):
        if self.head is None:
            return
        curr = self.head
        prev = None
        while curr:
            if curr.data == value:
                # if prev exists i.e if it is not none
                if prev:
                    prev.next = curr.next   
                #if prev doesnt exist and is none, that means curr is still self.head   
                else:
                    self.head = curr.next
                    self.length-=1
                # move it to the next node  
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return self
    
    #5 - incomplete
    def isPalindrome(self):
        if self.head is None:
            return
        curr = self.head
        currx2 = self.head
        
        while currx2 and currx2.next:
            curr = curr.next
            currx2 = currx2.next.next
        print(curr.data)
        print(currx2.data)
        #now, curr is in the middle and currx2 is at the end
        # temp = self.head
        # while temp:
        #     if temp == currx2:
        #         temp = temp.next
        #         curr
        
     #6-not working   
    def deleteNode(self, value):
        newNode = Node(value)
        if self.head is None:
            return
        temp = self.head
        while temp and temp.next:
            if newNode.data == temp.data:
                temp.data = temp.next.data
                temp.next = temp.next.next
            else:
                temp = temp.next
        return self
    
    #8-merge nodes - epic fail
    def mergeBetweenZeros(self):
        if self.head is None:
            return
        sum = 0
        curr = self.head
        while curr:
            if curr.data != 0:
                sum+=int(curr.data)
            else:
                curr = curr.next
            curr = curr.next
        print (sum)
        return self
        
        
        
        
myList = LinkedList(5)
myList.addToTheBeginning(8)
myList.addToTheBeginning(9)
myList.addToTheBeginning(6)
myList.addToTheEnd(0)
myList.addToTheEnd(3)
myList.addToTheEnd(7)
myList.getAtIndex(5)
myList.getAtIndexFromTheEnd(1)
myList.removeAtIndexFromTheEnd(10)
# myList.setAtIndex(4,20)
myList.printList()
myList.printListLength()

sortedList1 = LinkedList(1)
sortedList1.addToTheEnd(2)
sortedList1.addToTheEnd(4)

sortedList2 = LinkedList(1)
sortedList2.addToTheEnd(1)
sortedList2.addToTheEnd(1)
sortedList2.addToTheEnd(0)
sortedList2.addToTheEnd(3)
sortedList2.addToTheEnd(3)
sortedList2.addToTheEnd(4)
sortedList2.addToTheEnd(4)
sortedList2.addToTheEnd(4)
sortedList2.addToTheEnd(0)
sortedList2.addToTheEnd(4)
sortedList2.addToTheEnd(4)
sortedList2.addToTheEnd(5)
sortedList2.addToTheEnd(5)
sortedList2.addToTheEnd(7)
sortedList2.addToTheEnd(7)
sortedList2.addToTheEnd(7)
sortedList2.addToTheEnd(7)
sortedList2.addToTheEnd(7)
sortedList2.addToTheEnd(8)
sortedList2.removeElement(7)
sortedList2.deleteNode(8)
sortedList2.mergeBetweenZeros()
# sortedList2.removeDuplicates()
# sortedList2.deleteDuplicates()
sortedList2.printList()

