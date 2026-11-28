# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        ans = []
        
        if not root:
            return ans
        self.q = deque([root])
        while self.q:
            size = len(self.q)
            for i in range(size):
                root = self.q.popleft()
                if root.left:
                    self.q.append(root.left)
                if root.right:
                    self.q.append(root.right)
                if i == size - 1:
                    ans.append(root.val)
        return ans