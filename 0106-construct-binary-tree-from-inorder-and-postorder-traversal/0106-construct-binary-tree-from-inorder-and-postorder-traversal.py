# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        index_of = {}
        for i in range(len(inorder)):
            index_of[inorder[i]] = i
        self.post_id = len(postorder) - 1

        def build(left, right):
            if left > right:
                return None
            root_val = postorder[self.post_id]
            self.post_id -= 1
            root = TreeNode(root_val)
            mid = index_of[root.val]
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)
            return root
        return build(0, len(postorder) - 1)