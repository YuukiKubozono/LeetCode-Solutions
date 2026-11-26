# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def finder(node, goal, path):
            if not node:
                return False
            path.append(node)
            if node == goal:
                return True
            if finder(node.left, goal, path):
                return True
            if finder(node.right, goal, path):
                return True
            path.pop()
            return False

        path_p = []
        finder(root, p, path_p)
        path_q = []
        finder(root, q, path_q)

        ans = root
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i] != path_q[i]:
                break
            ans = path_p[i]

        return ans