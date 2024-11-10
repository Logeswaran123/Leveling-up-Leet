"""

---
MEDIUM
287. Find the Duplicate Number
---

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?

"""


## Solution 1
## Slow and Fast Pointer (Floyd's Tortoise and Hare)
## Neetcode explains this problem well (check it out!)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


## Solution 2
## Negative Marking
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums :
            idx = abs(num) - 1 
            if nums[idx] < 0 :
                return abs(num)
            nums[idx] *= -1
        return -1


## Solution 3
## Binary Search
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 1, n - 1
        while low < high:
            mid = low + (high - low) // 2
            count = sum(1 for num in nums if num <= mid)

            if count <= mid: # Duplicate can be in nums[mid+1] to nums[-1]
                low = mid + 1
            else:   # Duplicate can be in nums[0] to nums[mid]
                high = mid

        return low


## Solution 4
## Hash set
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num in visited: return num
            visited.add(num)
        return -1


## Solution 5
## Bit Manipulation
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for b in range(32):
            x = y = 0
            mask = 1 << b
            for num in nums:
                if num & mask:
                    x += 1

            for num in range(1, n):
                if num & mask:
                    y += 1

            if x > y:
                res |= mask

        return res