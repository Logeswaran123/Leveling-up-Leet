"""

---
MEDIUM
417. Pacific Atlantic Water Flow
---

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

"""

## Solution 1
#
# The function finds cells in a 2D grid (heights) that can flow water
# to both the Pacific and Atlantic oceans. Water can only flow from a cell to its neighboring
# cell if the neighboring cell is of equal or lower height.
#
# Example input: heights = [
#     [1, 2, 2, 3, 5],
#     [3, 2, 3, 4, 4],
#     [2, 4, 5, 3, 1],
#     [6, 7, 1, 4, 5],
#     [5, 1, 1, 2, 4]
# ]
#
# Step-by-step logic:
# 1. We initialize two sets: `pacific` and `atlantic` to keep track of cells that can
#    flow to the respective oceans.
# 2. The `dfs` function is used to perform a Depth-First Search starting from a cell.
#    This function checks the four neighboring cells (up, down, left, right) and adds
#    cells to the `visited` set if water can flow to them (i.e., their height is equal
#    to or greater than the current cell).
# 3. We run DFS starting from the cells adjacent to the Pacific and Atlantic oceans:
#    - For the Pacific Ocean, we start from the first row and the first column.
#    - For the Atlantic Ocean, we start from the last row and the last column.
#    This ensures that we explore all cells that can reach the respective oceans.
#
# 4. For each cell in the grid, we check if it is present in both `pacific` and `atlantic` sets.
#    If it is, that means water from that cell can flow to both oceans.
# 5. We collect all such cells and return them.
#
# Let's go through a partial example with the input provided:
# Starting from the Pacific (left and top edges):
# - Top-left cell (0, 0) with height 1 can flow to the Pacific (directly on the edge).
# - From (0, 0), DFS explores neighboring cells like (0, 1) with height 2, then (0, 2) with height 2, etc.
# - It continues to mark cells that can flow into the Pacific by comparing heights.
#
# Starting from the Atlantic (right and bottom edges):
# - Bottom-right cell (4, 4) with height 4 can flow to the Atlantic (directly on the edge).
# - From (4, 4), DFS explores neighboring cells like (3, 4) with height 5, (2, 4) with height 1, etc.
# - It continues to mark cells that can flow into the Atlantic.
#
# After running DFS for both oceans, the function checks which cells are in both the `pacific` and `atlantic` sets.
# In this example, the cells that can flow to both oceans are:
# [(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)]
#
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prev_height):
            if (
                min(r, c) < 0 or
                r >= rows or
                c >= cols or
                (r, c) in visited or
                heights[r][c] < prev_height
            ):
                return

            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # Start from first row (close to pacific) and 
        # Start from last row (close to atlantic) to 
        # find all the cells that reach pacific or atlantic from that starting cell
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        # Start from first column (close to pacific) and 
        # Start from last column (close to atlantic) to 
        # find all the cells that reach pacific or atlantic from that starting cell
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        # Return only the cells that can visit both pacific and atlantic
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append((r, c))

        return res