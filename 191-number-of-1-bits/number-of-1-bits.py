class Solution:
    def hammingWeight(self, n: int) -> int:
        k = 0
        num = n
        while num > 0:
            if num % 2 == 1:
                k += 1
            num = num // 2
        return k