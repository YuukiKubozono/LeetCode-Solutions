class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_step = 0
        max_step = 0
        for i in range(len(nums) - 1):
            max_step = max(max_step, i + nums[i])
            if i == current_step:
                jumps += 1
                current_step = max_step
            if current_step >= len(nums) -1:
                break
        return jumps