class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        still = 0
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                still = 0
                nums[k] = nums[i]
                k += 1
            else:
                still += 1
                if still <= 1:
                    nums[k] = nums[i]
                    k += 1
                else:
                    continue
        return k
            
            
