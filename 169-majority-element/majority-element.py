class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        k=nums[n//2]
        return k