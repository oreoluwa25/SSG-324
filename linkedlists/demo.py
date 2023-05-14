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

    # insert at the end - push

    def insert_at_end(self, data):
        # create a new node with the value
        newNode = Node(data)
        # check if the linked list is empty
        if self.head is None:
            # set the new node to the head and tail of the linked list
            self.head = newNode
            self.tail = newNode
        else:
            # set the next of the tail to the new node and change the tail to the new node
            self.tail.next = newNode
            self.tail = newNode
        # add one to the length
        self.length += 1
        return self

    # remove at the end - pop
    def remove_at_end(self):
        # check if the list is empty
        if self.head is None:
            print("Linked list is empty")
            return
        # store the head in two variables:temp and pre
        temp = self.head
        pre = self.head

        # checking the next value of temp
        while temp.next:
            # set pre to temp
            pre = temp
            # set temp to the next node
            temp = temp.next
        # the tail becomes the pre(since we're removing the next one)
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return self

    # remove from the beginning
    def remove_from_beginning(self):
        if self.head is None:
            print("Linked list is empty")
            return
        #
        curr = self.head
        self.head = self.head.next

        if self.length == 0:
            self.head = None
            self.tail = None
        curr.next = None
        return self

    # set method trial
    # time complexity - O(n)
    def replace_element(self, old_data, new_data):
        if self.head is None:
            raise Exception("the linkedlist is empty")
        if old_data == new_data:
            return
        node = self.head
        while node is not None:
            if node.data == old_data:
                node.data = new_data
                return
            node = node.next
        raise Exception("node not found")

    # get method trial
    # time complexity - O(n)
    def get_element(self, index):
        if self.head is None:
            print("the linkedlist is empty")
        count = 0
        curr = self.head
        while curr:
            if count == index:
                print(curr.data)
                return
            else:
                count += 1
                curr = curr.next
        print("node not found")
        return curr

    def get_node(self, index):
        if (index < 0 or index >= self.length):
            print("out of bounds")
            return
        temp = self.head
        for i in range(index):
            temp = temp.next

        return temp

    def set_node(self, index, value):
        temp = self.get_node(index)
        temp.data = value
        return self

    def insert_element(self, index, value):
        newNode = Node(value)
        prev = self.get_node(index - 1)
        temp = prev.next
        newNode.next = temp
        prev.next = newNode
        self.length += 1
        return self

    def remove_element(self, index):
        temp = self.get_node(index - 1)
        if (index == 0):
            self.remove_from_beginning()
            return
        if (index == self.length - 1):
            self.remove_at_end()
            return
        temp.next = temp.next.next

        self.length -= 1
        return self

    def middleNode(self):
        moveByTwo = self.head
        moveByOne = self.head
        while moveByTwo and moveByTwo.next:
            moveByOne = moveByOne.next
            moveByTwo = moveByTwo.next.next
        middle = moveByOne
        while middle:
            print(middle.data)
            middle = middle.next
        return self
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail= temp
        next = temp.next
        prev = None
        
        for i in range(self.length):
            next= temp.next
            temp.next = prev
            prev = temp
            temp = next
        return self 


myList = LinkedList(7)
myList.insert_at_end(11)
myList.insert_at_end(18)
myList.insert_at_end(25)
myList.insert_at_end(32)
myList.remove_element(2)

# myList.insert_at_end(37)
# myList.middleNode()
# print(myList.head.next.next.data)
# myList.remove_from_beginning()
# myList.replace_element(18,21)
# myList.get_element(1)
# print(myList.get_node(2))
# (myList.set_node(2,22))
# myList.middleNode()
value = myList.head
while value:
    print(value.data)
    value = value.next
