"""

---
EASY
217. Contains Duplicate
---

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109


"""

## Solution 1
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> nums_set;

        for(int i=0; i<nums.size(); i++) {
            if (nums_set.find(nums[i]) != nums_set.end()) {
                return true;
            }
            nums_set.insert(nums[i]);
        }
        return false;
    }
};


## Solution 2
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> nums_set;
        nums_set.insert(nums.begin(), nums.end());
        return true ? nums.size() > nums_set.size() : false;
    }
};