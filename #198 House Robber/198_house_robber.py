"""

---
MEDIUM
198. House Robber
---

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

"""

## Solution 1
# Important Dynamic Programming problem
#
# Example:
# Let's take `nums = [2, 7, 9, 3, 1]`.
# Here’s how the logic flows:
#
# Initialize n1 and n2 as 0:
# n1 (two houses back) = 0, n2 (previous house) = 0
#
# Iterate through each house in `nums`:
# - House 1 with money 2:
#   - temp = max(n1 + 2, n2) = max(0 + 2, 0) = 2
#   - Update n1 = n2 (0), and n2 = temp (2)
# - House 2 with money 7:
#   - temp = max(n1 + 7, n2) = max(0 + 7, 2) = 7
#   - Update n1 = n2 (2), and n2 = temp (7)
# - House 3 with money 9:
#   - temp = max(n1 + 9, n2) = max(2 + 9, 7) = 11
#   - Update n1 = n2 (7), and n2 = temp (11)
# - House 4 with money 3:
#   - temp = max(n1 + 3, n2) = max(7 + 3, 11) = 11
#   - Update n1 = n2 (11), and n2 = temp (11)
# - House 5 with money 1:
#   - temp = max(n1 + 1, n2) = max(11 + 1, 11) = 12
#   - Update n1 = n2 (11), and n2 = temp (12)
#
# After iterating through all houses, Return n2 (12), which is the maximum money we can rob.
class Solution:
    def rob(self, nums: List[int]) -> int:
        n1, n2 = 0, 0

        for num in nums:
            temp = max(n1 + num, n2)
            n1 = n2
            n2 = temp

        return n2