class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        points.sort()
        ans = 1
        left = float('-inf')
        right = float('inf')
        for xleft, xright in points:
            left = xleft
            if xleft <= right:
                right = min(xright, right)
            else:
                right = xright
                ans += 1
        return ans
