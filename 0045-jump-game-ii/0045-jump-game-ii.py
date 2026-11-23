class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        step = 1
        farthest = nums[0]
        end = nums[0]
        for i in range(n):
            if n - 1 <= end:
                break
            farthest = max(farthest, i + nums[i])
            if i == end:
                end = farthest
                step += 1
            
        return step