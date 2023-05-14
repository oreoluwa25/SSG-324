class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
        
class Solution:
    def flatten(self, head):
        if not head:
            return head
        
        dummy = Node(0)
        curr, stack = dummy, [head]
        
        while stack:
            temp = stack.pop()
            if temp.next:
                stack.append(temp.next)
            if temp.child:
                stack.append(temp.child)
                
            curr.next = temp
            temp.prev = curr
            temp.child = None
            curr = temp
        dummy.next.prev = None
        return dummy.next
    
    
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        curr = head

        while curr:
            if curr.child:
                childNode = curr.child
                childNode.prev = curr

                while childNode.next:
                    childNode = childNode.next
                childNode.next = curr.next

                if childNode.next:
                    childNode.next.prev = childNode
                curr.next = curr.child
                curr.child = None
            curr = curr.next
        return head