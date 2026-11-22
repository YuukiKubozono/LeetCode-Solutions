class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        total = 0
        start = 0
        time = float("inf")
        for end in range(len(nums)):
            total += nums[end]
            while total >= target:
                time = min(time, end - start + 1)
                total -= nums[start]
                start += 1
        
        if time == float("inf"):
            return 0
        return time