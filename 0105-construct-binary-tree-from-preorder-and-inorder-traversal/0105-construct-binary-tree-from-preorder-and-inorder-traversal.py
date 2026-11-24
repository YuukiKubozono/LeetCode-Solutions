# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        index_of = {}
        for i in range(len(inorder)):
            index_of[inorder[i]] = i
        self.pre_id = 0

        def build(left, right):
            if left > right:
                return None
            root_val = preorder[self.pre_id]
            self.pre_id += 1
            root = TreeNode(root_val)
            mid = index_of[root.val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        return build(0, len(inorder) - 1)
