class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        interval = points[0]
        start = 0
        end = 1
        shot = 1
        for point in points:
            if point[start] <= interval[end]:
                interval = [max(interval[start], point[start]), min(interval[end], point[end])]
            else:
                interval = point
                shot += 1
        return shot