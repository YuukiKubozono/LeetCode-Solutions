# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_node = root
        left_depth = 0
        while left_node:
            left_depth += 1
            left_node = left_node.left
        
        right_node = root
        right_depth = 0
        while right_node:
            right_depth += 1
            right_node = right_node.right
        
        if left_depth == right_depth:
            return 2**(left_depth) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
            
        
            