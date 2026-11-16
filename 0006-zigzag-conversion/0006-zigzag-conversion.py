class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = []
        for i in range(numRows):
            ans.append([])
        place = 0
        for x in s:
            if place < numRows - 1:
                ans[abs(place)].append(x)
                place += 1
            elif place == numRows - 1:
                ans[place].append(x)
                place *= -1
                place += 1
        for i in range(len(ans)):
            ans[i] = "".join(ans[i])
        ans = "".join(ans)
        return ans