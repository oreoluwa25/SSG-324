class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class BrowserHistory:
    def __init__(self, homepage):
        newNode = Node(homepage)
        self.head = newNode
        self.tail = newNode
        self.current = 0

    def printHistory(self):
        curr = self.head
        list = []
        while curr:
            list.append(curr.data)
            curr = curr.next
        print(list)
        return list

    def visit(self, url):
        newNode = Node(url)
        last = self.tail
        self.tail = newNode
        last.next = newNode
        self.current += 1
        return self
        # newNode.prev = self.head
        # self.head.next = newNode
        # self.head = self.head.next

    def back(self, steps):
        temp = self.head
        if self.current - steps < 0:
            print('out of bounds')
            return
        if steps < 0:
            print('out of bounds')

            return
        index = self.current - steps
        for i in range(index):
            temp = temp.next
        print(temp.data)
        self.current = index
        return temp.data
        # while (temp.prev and steps):
        #     temp = temp.prev
        #     steps-=1
        # print(temp.data)
        # return temp.data

    def forward(self, steps):
        curr = self.head
        temp = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        if steps+(self.current+1) > count:
            print('out of bounds')
            return
        if steps < 0:
            print('out of bounds')
            return
        for i in range(self.current):
            temp = temp.next
        for j in range(steps):
            temp = temp.next
            self.current += 1
        print(temp.data)
        return temp.data
        # while (temp.next and steps):
        #     temp = temp.next
        #     steps-=1
        # print(temp.data)
        # return temp.data


# myHistory = BrowserHistory('www.leetcode.com')
# myHistory.visit('www.google.com')
# myHistory.visit('www.facebook.com')
# myHistory.visit('www.youtube.com')
# myHistory.back(1)
# myHistory.back(1)
# myHistory.forward(1)
# myHistory.visit('www.linkedin.com')
# myHistory.forward(2)
# myHistory.back(2)
# myHistory.back(7)
# myHistory.printHistory()


# using leetcode
class History:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.current+1] + [url]
        self.current += 1

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history)-1, self.current+steps)
        return self.history[self.current]


history = History('www.bing.com')


l1 = [1, 2, 3]
new = 4
l1 = l1[:3] + [new]
print(l1)
