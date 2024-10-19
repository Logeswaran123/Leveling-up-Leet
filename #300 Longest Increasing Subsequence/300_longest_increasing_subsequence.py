"""

---
MEDIUM
300. Longest Increasing Subsequence
---

Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

"""

## Solution 1
## Dynamic Programming
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    cache[i] = max(cache[i], 1 + cache[j])

        return max(cache)


## Solution 2
## Efficient Solution
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        p = 1   # Length of the longest increasing subsequence
        for i in range(1, len(nums)):
            n = nums[i]

            # If the current number is greater than the last number in the current increasing subsequence,
            # we can extend the subsequence by including this number. So, we increase 'p'
            if n > nums[p - 1]: 
                p += 1

            # Use binary search (bisect_left) to find the position where `n` should be placed in the existing
            # increasing subsequence, ensuring that `nums` maintains a valid increasing subsequence up to `p-1`.
            # We replace the element at that position with `n`.
            nums[bisect.bisect_left(nums, n, hi=p - 1)] = n

        return p