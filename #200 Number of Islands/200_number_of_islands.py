"""

---
MEDIUM
200. Number of Islands
---

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

"""

## Solution 1
# Solution with Recursive DFS. Good to look at.
#
# Logic:
# Input grid:
# grid = [
#   ['1', '1', '0', '0', '0'],
#   ['1', '1', '0', '0', '1'],
#   ['0', '0', '0', '1', '1'],
#   ['0', '0', '0', '0', '0'],
#   ['1', '0', '1', '0', '1']
# ]
# 
# Process:
# - Start at the top-left corner (0,0):
#   - It's a '1' and not visited, so we found an island. Increment `num_islands` to 1.
#   - Perform DFS to mark all connected '1's around (0,0) as visited.
# - Continue scanning the grid:
#   - Skip all visited '1's.
#   - At (1,4), find another '1' that hasn't been visited. Increment `num_islands` to 2.
#   - Perform DFS to mark the connected '1's at (1,4) and (2,4) as visited.
# - Continue scanning:
#   - Find another island at (4,0). Increment `num_islands` to 3.
#   - Find another island at (4,2). Increment `num_islands` to 4.
#   - Finally, find another island at (4,4). Increment `num_islands` to 5.
#
# Output:
# The function returns 5, indicating there are 5 separate islands in the grid.
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0
        visited = set() # Keep track of all the visited "1"s
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r < 0 or r >= rows or c < 0 or c >= cols or
                grid[r][c] == "0" or
                (r, c) in visited
            ):
                return

            visited.add((r, c))

            # Check the neighbors and add them to visited
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    num_islands += 1
                    dfs(r, c)

        return num_islands
