class Node:
    def __init__(ore, data=None, next=None):
        ore.data = data
        ore.next = next
        
class LinkedList:
    def __init__(ore, value):
        newNode = Node(value)
        ore.head = newNode
        ore.tail = newNode
        ore.length = 1
        
    def printList(ore):
        node = ore.head
        liststr = ''
        while node:
            if node.next is None:
                liststr += str(node.data)
                break
            else:
                liststr+= str(node.data) + '-->'
                node = node.next
        print(liststr)
    
    
    
newList = LinkedList(7)
newList.printList()
    