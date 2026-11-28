# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        self.d = {}
        for i in range(len(inorder)):
            self.d[inorder[i]] = i
        self.id = 0

        def build(left, right):
            if left > right:
                return
            root = TreeNode(preorder[self.id])
            mid = self.d[root.val]
            self.id += 1
            root.left = build(left, mid - 1)    
            root.right = build(mid + 1, right)
            return root
        return build(0, len(preorder) - 1)