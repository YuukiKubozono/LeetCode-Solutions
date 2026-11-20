# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        start = dummy
        last = dummy
        for _ in range(n):
            last = last.next
        
        while last.next:
            start = start.next
            last = last.next
        
        sign = start.next.next
        start.next = sign
        return dummy.next