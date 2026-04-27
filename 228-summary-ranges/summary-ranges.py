class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:return []
        start = nums[0]
        ans = []
        for i in range(1,len(nums)):
            if nums[i-1] + 1 != nums[i]:
                end = nums[i-1]
                if start != end:
                    ans.append(f"{start}->{end}")
                else:
                    ans.append(f"{start}")
                start = nums[i]
            else:
                continue
        
        end = nums[-1]
        
        if start != end:
            ans.append(f"{start}->{end}")
        else:
            ans.append(f"{start}")
        return ans        

