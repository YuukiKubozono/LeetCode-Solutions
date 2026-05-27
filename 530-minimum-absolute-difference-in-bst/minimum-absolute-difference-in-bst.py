# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minDiff = float('inf')
        self.prevnode = None

        def see(node: Optional[TreeNode]):
            if node.left:
                see(node.left)

            if self.prevnode:
                diff = abs(node.val - self.prevnode.val)
                self.minDiff = min(self.minDiff, diff)
            
            self.prevnode = node

            if node.right:
                see(node.right)
        
        see(root)

        return self.minDiff
        

        