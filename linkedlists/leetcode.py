    #1 - Remove Nth Node From End of List(leetcode version)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         temp = head
#         prev = head
#         curr = head
#         counter = 1
#         while curr and curr.next:
#             counter+=1
#             curr = curr.next
#         if n == counter:
#             head = head.next
#             return head
#         for i in range(n):
#             counter-=1
#         for j in range(counter):
#             prev = temp
#             temp = temp.next
#         prev.next = temp.next            
#         # if counter == 0:
#         #     head = None
#         return head