class Solution:
    def climbStairs(self, n: int) -> int:
        half = n // 2
        ans = 0
        for i in range(half + 1):
            mid = i // 2
            
            mat = 1
            for j in range(1, i + 1):
                mat *= (n - i - j + 1) / j
            
            ans += mat
            ans = int(ans)
        return ans
