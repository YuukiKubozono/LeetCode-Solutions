class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        start = 0
        end = 1
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][start] <= ans[-1][end]:
                ans[-1][start] = min(ans[-1][start], intervals[i][start])
                ans[-1][end] = max(ans[-1][end], intervals[i][end])
            else:
                ans.append([intervals[i][start], intervals[i][end]])
        return ans