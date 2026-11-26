# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.values = []
        self.inorder(root)
        self.i = -1

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        self.values.append(node.val)
        self.inorder(node.right)

    def next(self) -> int:
        self.i += 1
        return self.values[self.i]

    def hasNext(self) -> bool:
        return self.i + 1 < len(self.values)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()