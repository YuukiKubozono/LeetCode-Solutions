class Solution:
    def reverseBits(self, n: int) -> int:
        num = n
        ans = 0
        for _ in range(32):
            i = n & 1
            ans = (ans << 1) | i
            n = n >> 1
        return ans