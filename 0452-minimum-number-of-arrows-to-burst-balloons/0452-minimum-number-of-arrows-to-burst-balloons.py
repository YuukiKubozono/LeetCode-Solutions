class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        start = 0
        end = 1
        arrow = 1
        line = points[0][end]
        for i in range(1, len(points)):
            if line < points[i][start]:
                arrow += 1
                line = points[i][end]
            else:
                line = min(line, points[i][end])
        return arrow