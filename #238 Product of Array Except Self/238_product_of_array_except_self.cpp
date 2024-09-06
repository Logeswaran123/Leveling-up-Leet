/*

---
MEDIUM
238. Product of Array Except Self
---

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


*/

// Solution 1
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int size = nums.size();
        vector<int> output(size, 1);

        int prefix = 1;
        for (int i=0; i<size; i++) {
            output[i] = prefix;
            prefix *= nums[i]; 
        }

        int postfix = 1;
        for (int i=size-1; i>=0; i--) {
            output[i] *= postfix;
            postfix *= nums[i]; 
        }

        return output;
    }
};


// Solution 2
// This is using division operator, so not an acceptable solution according to the problem statement
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int size = nums.size();
        int prod = 1;
        int zero_counter = 0;

        for (int i=0; i<size; i++) {
            if (nums[i] != 0) prod *= nums[i];
            else zero_counter++;
        }

        for (int i=0; i<size; i++) {
            if (nums[i] == 0 && zero_counter == 1) nums[i] = prod;
            else if (zero_counter == 0) nums[i] = prod / nums[i];
            else if (zero_counter != 0) nums[i] = 0;
        }

        return nums;
    }
};