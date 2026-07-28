class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        nums = x
        ans = 0
        while nums > 0:
            ans *= 10
            i = nums % 10
            nums //= 10
            ans += i
        return ans == x