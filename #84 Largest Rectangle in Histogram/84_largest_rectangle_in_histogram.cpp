/*

---
HARD
84. Largest Rectangle in Histogram
---

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104

*/

// Solution 1
// Monotonic Stack
//
// The algorithm uses a monotonic stack to efficiently compute the largest rectangle in a histogram in O(n) time.
//
// **Logic:**
// 1. The stack stores pairs of (index, height) in increasing order of height.
// 2. For each bar in the histogram:
//  - If the current bar is taller than the bar at the top of the stack, push it onto the stack.
//  - If the current bar is shorter, it means we can compute the area of rectangles formed with the bars in the stack
//    (as the current bar acts as the right boundary for those rectangles). We repeatedly pop from the stack,
//    calculate the area, and track the maximum area.
//
// 3. After iterating through all bars, some bars may still be left in the stack. For these, calculate the area using the
//  length of the histogram as the right boundary.
//
// **Example:**
// Given heights = [2, 1, 5, 6, 2, 3]:
// - Step 1: Start with an empty stack and iterate through the bars:
// i = 0, h = 2: Push (0, 2) onto the stack. Stack: [(0, 2)]
// i = 1, h = 1: Pop (0, 2), calculate area = 2 * (1 - 0) = 2. Push (0, 1). Stack: [(0, 1)]
// i = 2, h = 5: Push (2, 5). Stack: [(0, 1), (2, 5)]
// i = 3, h = 6: Push (3, 6). Stack: [(0, 1), (2, 5), (3, 6)]
// i = 4, h = 2: Pop (3, 6), calculate area = 6 * (4 - 3) = 6.
//               Pop (2, 5), calculate area = 5 * (4 - 2) = 10. Push (2, 2). Stack: [(0, 1), (2, 2)]
// i = 5, h = 3: Push (5, 3). Stack: [(0, 1), (2, 2), (5, 3)]
//
// - Step 2: Process remaining bars in the stack:
// Pop (5, 3), calculate area = 3 * (6 - 5) = 3.
// Pop (2, 2), calculate area = 2 * (6 - 2) = 8.
// Pop (0, 1), calculate area = 1 * (6 - 0) = 6.
//
// - Max area = 10.
//
// **Result:** The largest rectangle area is 10.
//
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int max_area = 0;
        std::stack<std::pair<int, int>> stack; // pair: (index, height)

        for (int i = 0; i < heights.size(); ++i) {
            int start = i;
            while (!stack.empty() && stack.top().second > heights[i]) {
                auto [idx, height] = stack.top();
                stack.pop();
                max_area = std::max(max_area, height * (i - idx));
                start = idx;
            }
            stack.emplace(start, heights[i]);
        }

        while (!stack.empty()) {
            auto [idx, height] = stack.top();
            stack.pop();
            max_area = std::max(max_area, height * (static_cast<int>(heights.size()) - idx));
        }

        return max_area;
    }
};