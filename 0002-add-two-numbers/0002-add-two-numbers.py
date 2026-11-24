# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        ans = ListNode()
        dummy = ans
        count = 0

        while l1 or l2 or count:
            total = count
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            count = total // 10
            ans.next = ListNode(total % 10)
            ans = ans.next
        return dummy.next