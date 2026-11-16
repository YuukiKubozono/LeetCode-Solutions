class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda p:p[1])
        arrow = points[0][1]
        shot = 1
        for start, end in points:
            if arrow < start:
                arrow = end
                shot += 1
        return shot