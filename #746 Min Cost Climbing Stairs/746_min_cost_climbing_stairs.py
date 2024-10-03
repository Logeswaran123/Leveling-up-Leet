"""

---
EASY
746. Min Cost Climbing Stairs
---

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999

"""

## Solution 1
# Bottom-up Dynamic Programming
#
# Example:
# Input: cost = [10, 15, 20]
# Explanation:
# - The goal is to reach the top of the stairs, and you can start at step 0 or step 1.
# - You can either step 1 or step 2 at a time, and the cost at each step is given by the input array.
#
# Step-by-step explanation:
# cost = [10, 15, 20]
# First, append 0 at the end to represent the top floor:
# cost = [10, 15, 20, 0]
#
# Now, work backwards from step 2:
# For step 2: cost[2] = min(20 + cost[3], 20 + cost[4]) = min(20 + 0, 20) = 20
# For step 1: cost[1] = min(15 + cost[2], 15 + cost[3]) = min(15 + 20, 15 + 0) = 15
# For step 0: cost[0] = min(10 + cost[1], 10 + cost[2]) = min(10 + 15, 10 + 20) = 25
#
# Finally, return the minimum between cost[0] and cost[1]:
# return min(25, 15) = 15
#
# Output: 15
#
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)  # Top Floor cost

        # For each step, compute the minimal cost to reach the top from that step.
        for i in range(len(cost) - 3, -1, -1):
            # Update the cost at each step to be the current cost of that step
            # plus the minimum of the costs of the next one or two steps.
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])

        # Finally, return the minimum cost of starting from either the first step or second step.
        return min(cost[0], cost[1])