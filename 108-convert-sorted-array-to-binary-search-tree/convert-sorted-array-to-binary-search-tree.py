# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def change(list: Optional[list]):
            if not list:
                return None
            mid = len(list) // 2

            root = TreeNode(list[mid])

            root.left = change(list[:mid])
            root.right = change(list[mid + 1:])

            return root
        
        ans = change(nums)
        return ans
