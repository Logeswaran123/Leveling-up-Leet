"""

---
EASY
70. Climbing Stairs
---

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

"""

## Solution 1
# Bottom-up Dynamic Programming
#
# Example: n = 4
# The tree structure for climbing 4 steps will look like this,
#                0
#              /   \
#            1       2
#          /   \    /   \
#        2      3  3     4
#      /   \    |   |
#     3     4   4   4
#    /
#   4
#
class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2 = 1, 1

        for _ in range(n - 1):
            temp = n1
            n1 = n1 + n2
            n2 = temp

        return n1

## Solution 2
# Bottom-up Dynamic Programming
class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2 = 1, 1

        for _ in range(n - 1):
            temp = n1
            n1 = n1 + n2
            n2 = temp

        return n1