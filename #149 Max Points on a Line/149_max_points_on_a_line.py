"""

---
HARD
149. Max Points on a Line
---

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 3


Example 2:

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

"""

## Solution 1
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1
        for i in range(len(points)):
            p1 = points[i]
            count = collections.defaultdict(int)
            for j in range(i+1, len(points)):
                p2 = points[j]
                if p1[0] == p2[0]: # same X value, so slope is inf
                    slope = float("inf")
                else: # calculate slope with mathematical formula
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                count[slope] += 1
                res = max(res, count[slope] + 1)
        return res