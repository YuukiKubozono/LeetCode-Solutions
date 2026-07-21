class Solution:
    def reverseBits(self, n: int) -> int:
        num = n
        k = []
        for _ in range(32):
            if num % 2 == 0:
                k.append(0)
            else:
                k.append(1)
            num = num // 2
        k.reverse()
        ans = 0
        for j in range(len(k)):
            ans += k[j] * 2 ** (j)

        return ans