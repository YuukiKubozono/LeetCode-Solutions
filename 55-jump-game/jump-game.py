class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_step = 0
        for i in range(len(nums)):
            if max_step < i:
                return False
            else:
                max_step = max(max_step, i + nums[i])
        
        return True