class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def help(left, right):
            if left > right:
                return left
            
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return help(mid + 1, right)
            elif nums[mid] > target:
                return help(left, mid - 1)
            
        return help(0, len(nums) - 1)
