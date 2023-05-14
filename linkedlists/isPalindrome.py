# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None

        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr
            
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
    
mySol = Solution()
myNode = ListNode(8)
print(mySol.isPalindrome(myNode))