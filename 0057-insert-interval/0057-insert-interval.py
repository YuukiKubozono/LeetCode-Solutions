class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        start = 0
        end = 1
        ans = []
        placed = False
        for interval in intervals:
            if interval[end] < newInterval[start]:
                ans.append(interval)
            elif newInterval[end] < interval[start]:
                if not placed:
                    ans.append(newInterval)
                    placed = True
                ans.append(interval)
            else:
                newInterval = [min(newInterval[start], interval[start]), max(newInterval[end], interval[end])]
        if not placed:
            ans.append(newInterval)
        return ans
            