/*

---
HARD
239. Sliding Window Maximum
---

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

*/

// Solution 1
// Sliding Window
//
//
// The function 'maxSlidingWindow' finds the maximum in every sliding window of size 'k' in the list 'nums'.
// Example:
// nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
// Sliding windows:
// [1, 3, -1] -> max = 3
// [3, -1, -3] -> max = 3
// [-1, -3, 5] -> max = 5
// [-3, 5, 3] -> max = 5
// [5, 3, 6] -> max = 6
// [3, 6, 7] -> max = 7
// Output: [3, 3, 5, 5, 6, 7]
// 
// The algorithm uses a deque to store indices of 'nums' such that:
// 1. The elements in the deque are in decreasing order of value (to keep the max at the front).
// 2. Indices that are no longer in the current window are removed from the front of the deque.
//
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> output;
        deque<int> q; // Store indices
        int l = 0, r = 0;

        while (r < nums.size()) {
            // Remove smaller elements from the back of deque
            while (!q.empty() && nums[q.back()] < nums[r]) {
                q.pop_back();
            }
            q.push_back(r);

            // Remove the leftmost element if it's outside the window
            if (l > q.front()) {
                q.pop_front();
            }

            // Add the maximum to the output once the window size is reached
            if ((r + 1) >= k) {
                output.push_back(nums[q.front()]);
                l++;
            }
            r++;
        }

        return output;
    }
};