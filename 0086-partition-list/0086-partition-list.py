# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        small_dummy = ListNode(0)
        big_dummy = ListNode(0)
        small_last = small_dummy
        big_last = big_dummy
        cur = head

        while cur:
            if cur.val < x:
                small_last.next = cur
                small_last = cur
            else:
                big_last.next = cur
                big_last = cur
            cur = cur.next
        
        big_last.next = None
        small_last.next = big_dummy.next
        return small_dummy.next