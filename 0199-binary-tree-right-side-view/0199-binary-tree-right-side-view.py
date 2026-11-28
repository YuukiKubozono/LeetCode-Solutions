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
        
        def dfs(node, depth):
            if not node:
                return
            if depth == len(ans):
                ans.append(node.val)
            if node.right:
                dfs(node.right, depth + 1)
            if node.left:
                dfs(node.left, depth + 1)
        dfs(root, 0)
        return ans