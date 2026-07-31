class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        num = 0
        for i in range(n):
            num += digits[n - 1 - i] * 10**(i)
        ans = num + 1
        list_ans = []
        while ans > 0:
            list_ans.append(ans % 10)
            ans = ans // 10
        list_ans.reverse()
        return list_ans