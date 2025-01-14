"""

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

"""

## Solution 1
## Sliding Window
#
# The function 'maxSlidingWindow' finds the maximum in every sliding window of size 'k' in the list 'nums'.
# Example:
# nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
# Sliding windows:
# [1, 3, -1] -> max = 3
# [3, -1, -3] -> max = 3
# [-1, -3, 5] -> max = 5
# [-3, 5, 3] -> max = 5
# [5, 3, 6] -> max = 6
# [3, 6, 7] -> max = 7
# Output: [3, 3, 5, 5, 6, 7]
# 
# The algorithm uses a deque to store indices of 'nums' such that:
# 1. The elements in the deque are in decreasing order of value (to keep the max at the front).
# 2. Indices that are no longer in the current window are removed from the front of the deque.
#
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # lets store index here
        l = r = 0

        while r < len(nums):
            # Remove smaller elements from the back of deque
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove the leftmost element if it's outside the window
            if l > q[0]:
                q.popleft()

            # Add the maximum to the output once the window size is reached
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output