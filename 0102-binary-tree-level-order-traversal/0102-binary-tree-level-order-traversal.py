# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        ans = []
        if not root:
            return ans
        self.q = deque([root])
        self.id = 0

        while self.q:
            ans.append([])
            size = len(self.q)
            
            for i in range(size):
                node = self.q.popleft()
                if i <= size - 1:
                    ans[self.id].append(node.val)
                if node.left:
                    self.q.append(node.left)
                if node.right:
                    self.q.append(node.right)
            self.id += 1
        return ans