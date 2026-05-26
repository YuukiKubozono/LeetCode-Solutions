# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        q = []
        def Put(node):
            if not node:
                return
            q.append(node.val)
            Put(node.left)
            Put(node.right)
        Put(root)
        q.sort()

        ans = float('inf')
        for i in range(1, len(q)):
            diff = q[i] - q[i-1]
            if ans > diff:
                ans = diff
        return ans
        