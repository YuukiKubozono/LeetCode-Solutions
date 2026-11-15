class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for x in nums_set:
            val = x
            if val - 1 not in nums_set:
                count = 1
                while val + 1 in nums_set:
                    count += 1
                    val += 1
                ans = max(count, ans)
        return ans