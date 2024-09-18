/*

---
MEDIUM
286. Walls and Gates
---

You are given a m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}

*/

// Solution 1
// Good to look at this problem (common question). Solution uses custom hash function.
//
// The problem is that std::unordered_set is using std::hash template to compute hashes for its entries 
// and there is no std::hash specialization for pairs. So, we have to define our own custom function.
// Custom hash function for pair<int, int>
//
// Input Grid:
// [
//   [2147483647, -1,         0,          2147483647],
//   [2147483647, 2147483647, 2147483647, -1],
//   [2147483647, -1,         2147483647, -1],
//   [0,          -1,         2147483647, 2147483647]
// ]
//
// 1. Initialize the queue with all gates (cells with value 0):
//    - Gates are located at (0, 2) and (3, 0).
//    - Initial queue: [(0, 2), (3, 0)]
//    - Mark these cells as visited.
//
// 2. Start BFS with distance = 0. Increment distance after processing each level.
//
// 3. Distance = 0:
//    - Process (0, 2):
//      - Mark grid[0][2] as 0 (already set).
//      - Explore neighbors:
//        - (1, 2): Valid and unvisited. Mark as visited. Add to queue.
//        - (-1, 2): Out of bounds. Skip.
//        - (0, 3): Valid and unvisited. Mark as visited. Add to queue.
//        - (0, 1): Obstacle (-1). Skip.
//    - Process (3, 0):
//      - Mark grid[3][0] as 0 (already set).
//      - Explore neighbors:
//        - (4, 0): Out of bounds. Skip.
//        - (2, 0): Valid and unvisited. Mark as visited. Add to queue.
//        - (3, 1): Obstacle (-1). Skip.
//        - (3, -1): Out of bounds. Skip.
//    - Queue after this step: [(1, 2), (0, 3), (2, 0)]
//    - Increment distance to 1.
//
// 4. Distance = 1:
//    - Process (1, 2):
//      - Mark grid[1][2] as 1.
//      - Explore neighbors:
//        - (2, 2): Valid and unvisited. Mark as visited. Add to queue.
//        - (0, 2): Already visited. Skip.
//        - (1, 3): Obstacle (-1). Skip.
//        - (1, 1): Valid and unvisited. Mark as visited. Add to queue.
//    - Process (0, 3):
//      - Mark grid[0][3] as 1.
//      - Explore neighbors:
//        - (1, 3): Obstacle (-1). Skip.
//        - (-1, 3): Out of bounds. Skip.
//        - (0, 4): Out of bounds. Skip.
//        - (0, 2): Already visited. Skip.
//    - Process (2, 0):
//      - Mark grid[2][0] as 1.
//      - Explore neighbors:
//        - (3, 0): Already visited. Skip.
//        - (1, 0): Valid and unvisited. Mark as visited. Add to queue.
//        - (2, 1): Obstacle (-1). Skip.
//        - (2, -1): Out of bounds. Skip.
//    - Queue after this step: [(2, 2), (1, 1), (1, 0)]
//    - Increment distance to 2.
//
// 5. Distance = 2:
//    - Process (2, 2):
//      - Mark grid[2][2] as 2.
//      - Explore neighbors:
//        - (3, 2): Valid and unvisited. Mark as visited. Add to queue.
//        - (1, 2): Already visited. Skip.
//        - (2, 3): Obstacle (-1). Skip.
//        - (2, 1): Obstacle (-1). Skip.
//    - Process (1, 1):
//      - Mark grid[1][1] as 2.
//      - Explore neighbors:
//        - (2, 1): Obstacle (-1). Skip.
//        - (0, 1): Obstacle (-1). Skip.
//        - (1, 2): Already visited. Skip.
//        - (1, 0): Already visited. Skip.
//    - Process (1, 0):
//      - Mark grid[1][0] as 2.
//      - Explore neighbors:
//        - (2, 0): Already visited. Skip.
//        - (0, 0): Valid and unvisited. Mark as visited. Add to queue.
//        - (1, 1): Already visited. Skip.
//        - (1, -1): Out of bounds. Skip.
//    - Queue after this step: [(3, 2), (0, 0)]
//    - Increment distance to 3.
//
// 6. Distance = 3:
//    - Process (3, 2):
//      - Mark grid[3][2] as 3.
//      - Explore neighbors:
//        - (4, 2): Out of bounds. Skip.
//        - (2, 2): Already visited. Skip.
//        - (3, 3): Valid and unvisited. Mark as visited. Add to queue.
//        - (3, 1): Obstacle (-1). Skip.
//    - Process (0, 0):
//      - Mark grid[0][0] as 3.
//      - Explore neighbors:
//        - (1, 0): Already visited. Skip.
//        - (-1, 0): Out of bounds. Skip.
//        - (0, 1): Obstacle (-1). Skip.
//        - (0, -1): Out of bounds. Skip.
//    - Queue after this step: [(3, 3)]
//    - Increment distance to 4.
//
// 7. Distance = 4:
//    - Process (3, 3):
//      - Mark grid[3][3] as 4.
//      - Explore neighbors:
//        - (4, 3): Out of bounds. Skip.
//        - (2, 3): Obstacle (-1). Skip.
//        - (3, 4): Out of bounds. Skip.
//        - (3, 2): Already visited. Skip.
//    - Queue is now empty.
//
// Final grid after BFS:
// [
//   [3, -1,  0,  1],
//   [2,  2,  1, -1],
//   [1, -1,  2, -1],
//   [0, -1,  3,  4]
// ]
//
struct PairHash {
    size_t operator()(const pair<int, int>& p) const {
        return hash<int>()(p.first) ^ (hash<int>()(p.second) << 1);
    }
};

class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        unordered_set<pair<int, int>, PairHash> visited;
        queue<pair<int, int>> q;

        auto add_cell = [&](int r, int c) {
            if (r < 0 || c < 0 || r >= rows || c >= cols || 
                visited.count({r, c}) || grid[r][c] == -1) {
                return;
            }
            visited.insert({r, c});
            q.push({r, c});
        };

        // Check for Gates
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] == 0) {
                    visited.insert({r, c});
                    q.push({r, c});
                }
            }
        }

        int distance = 0;
        while (!q.empty()) {
            int q_size = q.size();
            for (int i = 0; i < q_size; ++i) {
                auto [r, c] = q.front();
                q.pop();
                grid[r][c] = distance;
                add_cell(r + 1, c);
                add_cell(r - 1, c);
                add_cell(r, c + 1);
                add_cell(r, c - 1);
            }
            ++distance;
        }
    }
};
