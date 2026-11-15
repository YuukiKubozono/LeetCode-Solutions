class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        times = 1
        k = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                times += 1
            else:
                times = 1
            if times < 3:
                k += 1
                nums[k] = nums[i]
        return k + 1