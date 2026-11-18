# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        val = 0
        head = ListNode(0)
        ans = head
        while (l1 is not None) or (l2 is not None) or (val != 0):
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if l2 is not None:
                val += l2.val
                l2 = l2.next
            ans.next = ListNode(val % 10)
            ans = ans.next
            val = val // 10
        return head.next