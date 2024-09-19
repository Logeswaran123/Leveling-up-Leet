/*

---
MEDIUM
994. Rotting Oranges
---

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

*/

// Solution 1
// Multisource BFS
// Similar to #286. Check #286 for example explanation.
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        queue<pair<int, int>> q;
        int num_fresh_oranges = 0;

        // Check for Rotten Oranges and Count Fresh Oranges
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] == 2) q.push({r, c});
                if (grid[r][c] == 1) num_fresh_oranges++;
            }
        }

        auto add_cell = [&](int r, int c) {
            if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] != 1) {
                return;
            }

            grid[r][c] = 2;
            q.push({r, c});
            num_fresh_oranges--;
        };

        int time = 0;
        while (!q.empty() && num_fresh_oranges > 0) {
            int q_size = q.size();
            for (int i = 0; i < q_size; ++i) {
                auto [r, c] = q.front();
                q.pop();
                add_cell(r + 1, c);
                add_cell(r - 1, c);
                add_cell(r, c + 1);
                add_cell(r, c - 1);
            }
            ++time;
        }

        return (num_fresh_oranges == 0 ? time : -1);
    }
};