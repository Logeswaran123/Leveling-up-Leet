"""

---
MEDIUM
15. 3Sum
---

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""

## Solution 1
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if nums[0] >= 0:
            if nums[0] == nums[1] == nums[2] == 0:
                return [[0, 0, 0]]
            return []

        res = []
        for i in range(len(nums)):
            # check for repeated values
            if i != 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1
            target = -nums[i]
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[left], nums[right], nums[i]])
                    # skip over any repeated values
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else: # nums[left] + nums[right] > target:
                    right -= 1
        return res

## Solution 2
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if a > 0: # If pointer crosses 0 in sorted array
                break

            if i>0 and nums[i-1] == a: # Skip Duplicates
                continue

            l, r = i+1, len(nums)-1
            while (l<r):
                summed = a + nums[l] + nums[r]

                if (summed>0): r-=1
                elif (summed<0): l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r: # Skip Duplicates
                        l+=1

        return res