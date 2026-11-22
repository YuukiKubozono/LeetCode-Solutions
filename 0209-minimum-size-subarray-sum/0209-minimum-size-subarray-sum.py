class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ans = []
        total = 0
        time = float("inf")
        for x in nums:
            ans.append(x)
            total += x
            while total >= target:
                time = min(time, len(ans))
                total -= ans[0]
                ans.remove(ans[0])
        
        if time == float("inf"):
            return 0
        return time