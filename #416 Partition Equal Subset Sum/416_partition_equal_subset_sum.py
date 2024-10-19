"""

---
MEDIUM
416. Partition Equal Subset Sum
---

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100

"""

## Solution 1
## Dynamic Programming
#
# Example:
# For nums = [1, 5, 11, 5]
#
# The sum of the array is 1 + 5 + 11 + 5 = 22
# Since 22 is even, we can try to find two subsets that sum up to 22 / 2 = 11
#
# 1st iteration (i = 3, nums[3] = 5):
# dp = {0}, nextDP becomes {0, 5}
# 
# 2nd iteration (i = 2, nums[2] = 11):
# dp = {0, 5}, nextDP becomes {0, 5, 11, 16}
#
# 3rd iteration (i = 1, nums[1] = 5):
# dp = {0, 5, 11, 16}, nextDP becomes {0, 5, 10, 11, 16, 21}
# We found 11! So, the function returns True.
#
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:   # If sum is odd, we can't find a subset
            return False

        dp = set()  # cache
        dp.add(0)   # Base case
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target: # If can get the target by summing, return true
                    return True
                nextDP.add(t + nums[i]) #   Add sum to set
                nextDP.add(t)   # Add the already existing value bact to set
            dp = nextDP
        return False