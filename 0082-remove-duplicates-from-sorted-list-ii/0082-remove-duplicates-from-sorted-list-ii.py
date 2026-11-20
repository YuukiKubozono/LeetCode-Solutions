# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        while cur:
            if cur.next and cur.val == cur.next.val:
                dup_val = cur.val
                while cur and cur.val == dup_val:
                    cur = cur.next
                prev.next = cur                
            else:
                prev = cur
                cur = cur.next
                
        return dummy.next