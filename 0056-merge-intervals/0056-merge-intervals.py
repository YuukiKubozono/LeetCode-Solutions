class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        start = 0
        end = 1
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if ans[-1][end] < intervals[i][start]:
                ans.append(intervals[i])
            else:
                ans[-1] = [ans[-1][start], max(ans[-1][end], intervals[i][end])]
        return ans