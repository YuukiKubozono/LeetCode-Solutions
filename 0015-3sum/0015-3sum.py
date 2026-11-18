class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left = i + 1
            right = n - 1
            valid = - nums[i]
            while left < right:
                sum = nums[left] + nums[right]

                if sum == valid:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1                
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1                    
                elif sum < valid:
                    left += 1
                else:
                    right -= 1
        return ans
                