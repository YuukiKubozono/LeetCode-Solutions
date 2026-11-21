# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        count = 0
        dummy = ListNode(0, head)
        while head:
            count += 1
            head = head.next
        if count == 0:
            return dummy.next
        k %= count
        if k == 0:
            return dummy.next
        
        start = dummy.next
        cur = dummy
        last = dummy
        for _ in range(k):
            last = last.next
        
        while last.next:
            last = last.next
            cur = cur.next
        dummy.next = cur.next
        last.next = start
        cur.next = None
        
        return dummy.next

        