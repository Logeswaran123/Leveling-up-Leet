/*

---
MEDIUM
695. Max Area of Island
---

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

*/

// Solution 1
// Solution with Recursive DFS. Good to look at. Also look at #200
//
// Input grid:
// grid = [
//   [0, 0, 1, 0, 0],
//   [1, 1, 1, 0, 0],
//   [0, 1, 0, 0, 1],
//   [0, 0, 0, 1, 1],
//   [1, 1, 0, 0, 0]
// ]
//
// Process:
// - Start scanning the grid from the top-left:
//   - At (0, 2), find a '1'. It's not visited, so start a DFS to calculate its area:
//     - The DFS marks all connected '1's at (1, 2), (1, 1), (2, 1), and (1, 0).
//     - The total area of this island is 5.
//     - Update `area` to 5.
// - Continue scanning:
//   - Skip all visited cells that belong to the already counted island.
//   - At (2, 4), find another '1'. It's not visited, so start a DFS:
//     - The DFS marks connected '1's at (3, 4) and (3, 3).
//     - The total area of this island is 3.
//     - `area` remains 5, as it's larger than 3.
//   - At (4, 0), find another '1'. It's not visited, so start a DFS:
//     - The DFS marks the connected '1' at (4, 1).
//     - The total area of this island is 2.
//     - `area` remains 5, as it's larger than 2.
//
// Output:
// The function returns 5, indicating that the largest island in the grid has an area of 5.
//
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        if (grid.empty()) {
            return 0;
        }

        int area = 0;
        int rows = grid.size();
        int cols = grid[0].size();
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));  // Keep track of all the visited "1"s

        // Lambda function for DFS traversal
        auto dfs = [&](int r, int c, auto& dfs_ref) -> int {
            if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == 0 || visited[r][c]) {
                return 0;
            }

            visited[r][c] = true;

            // Check the neighbors (up, down, left, right)
            return 1 + dfs_ref(r + 1, c, dfs_ref) + dfs_ref(r - 1, c, dfs_ref) +
                        dfs_ref(r, c + 1, dfs_ref) + dfs_ref(r, c - 1, dfs_ref);
        };

        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] == 1 && !visited[r][c]) {
                    area = max(area, dfs(r, c, dfs));
                }
            }
        }

        return area;
    }
};