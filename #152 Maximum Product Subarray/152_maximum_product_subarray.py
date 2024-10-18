"""

---
MEDIUM
152. Maximum Product Subarray
---

Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

"""

## Solution 1
## Dynamic Programming
#
# Example:
# nums = [2, 3, -2, 4]
#
# Step-by-step:
# Start:
# res = 2 (first element)
# curr_min = 1, curr_max = 1
#
# First element (num = 2):
# tmp = curr_max * num = 1 * 2 = 2
# curr_max = max(2 * 1, 2 * 1, 2) = 2
# curr_min = min(2, 2 * 1, 2) = 2
# res = max(2, 2) = 2
#
# Second element (num = 3):
# tmp = curr_max * num = 2 * 3 = 6
# curr_max = max(2 * 3, 2 * 3, 3) = 6
# curr_min = min(6, 3 * 2, 3) = 3
# res = max(6, 2) = 6
#
# Third element (num = -2):
# tmp = curr_max * num = 6 * (-2) = -12
# curr_max = max(-12, -2 * 3, -2) = -2
# curr_min = min(-12, -2 * 3, -2) = -12
# res remains = 6
#
# Fourth element (num = 4):
# tmp = curr_max * num = -2 * 4 = -8
# curr_max = max(-8, 4 * (-12), 4) = 4
# curr_min = min(-8, 4 * (-12), 4) = -48
# res = max(6, 4) = 6
#
# Final result is 6, the maximum product of the subarray [2, 3].
#
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_min, curr_max = 1, 1

        for num in nums:
            tmp = curr_max * num    # Store the temporary max product before updating curr_max

            # Calculate the current maximum product by comparing three cases:
            # 1. Current number alone (start new subarray)
            # 2. Current number * previous max product
            # 3. Current number * previous min product (in case of negative flipping - this is important because multiplying two negatives gives a positive)
            curr_max = max(num * curr_max, num * curr_min, num)

            # Calculate the current minimum product similarly
            curr_min = min(tmp, num * curr_min, num)

            res = max(res, curr_max)    # Maximum found so far
        return res