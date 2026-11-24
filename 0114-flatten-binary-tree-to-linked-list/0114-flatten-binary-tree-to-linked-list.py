# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def put_in(node, new):
            store = node.right
            tail = new
            while tail.right:
                tail = tail.right
            node.right = new
            tail.right = store
            node.left = None
        cur = root
        while cur:
            while cur.left:
                put_in(cur, cur.left)
            cur = cur.right