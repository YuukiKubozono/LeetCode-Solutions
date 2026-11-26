class Solution:
    def jump(self, nums: list[int]) -> int:
        farthest = 0
        last_step = 0
        step = 0
        for i in range(len(nums)):
            farthest = max(farthest, i + nums[i])
            if i == last_step:
                if last_step < len(nums) - 1:
                    step += 1
                else:
                    break
                last_step = farthest
        return step