class Solution:
    def romanToInt(self, s: str) -> int:
        Roman_nums={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        ans=0
        for i in range(1,len(s)):
            if Roman_nums[s[i]]<=Roman_nums[s[i-1]]:
                ans+=Roman_nums[s[i-1]]
            else:
                ans-=Roman_nums[s[i-1]]
        ans+=Roman_nums[s[-1]]
        return ans