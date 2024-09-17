/*

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

*/

// Solution 1
// Solution with lambda function and Recursive DFS. Good to look at. Also look at #695
//
// Logic:
// Input grid:
// grid = [
//   ['1', '1', '0', '0', '0'],
//   ['1', '1', '0', '0', '1'],
//   ['0', '0', '0', '1', '1'],
//   ['0', '0', '0', '0', '0'],
//   ['1', '0', '1', '0', '1']
// ]
// 
// Process:
// - Start at the top-left corner (0,0):
//   - It's a '1' and not visited, so we found an island. Increment `num_islands` to 1.
//   - Perform DFS to mark all connected '1's around (0,0) as visited.
// - Continue scanning the grid:
//   - Skip all visited '1's.
//   - At (1,4), find another '1' that hasn't been visited. Increment `num_islands` to 2.
//   - Perform DFS to mark the connected '1's at (1,4) and (2,4) as visited.
// - Continue scanning:
//   - Find another island at (4,0). Increment `num_islands` to 3.
//   - Find another island at (4,2). Increment `num_islands` to 4.
//   - Finally, find another island at (4,4). Increment `num_islands` to 5.
//
// Output:
// The function returns 5, indicating there are 5 separate islands in the grid.
//
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) {
            return 0;
        }

        int num_islands = 0;
        int rows = grid.size();
        int cols = grid[0].size();
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));  // Keep track of all the visited "1"s

        // Lambda function for DFS traversal
        auto dfs = [&](int r, int c, auto& dfs_ref) -> void {
            if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == '0' || visited[r][c]) {
                return;
            }

            visited[r][c] = true;

            // Check the neighbors (up, down, left, right) and add them to visited
            dfs_ref(r + 1, c, dfs_ref);
            dfs_ref(r - 1, c, dfs_ref);
            dfs_ref(r, c + 1, dfs_ref);
            dfs_ref(r, c - 1, dfs_ref);
        };

        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] == '1' && !visited[r][c]) {
                    num_islands++;
                    dfs(r, c, dfs);
                }
            }
        }

        return num_islands;
    }
};