/*

---
HARD
42. Trapping Rain Water
---

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105


*/

// Solution 1
// Space Complexity: O(n)
class Solution {
public:
    int trap(vector<int>& height) {
        if(height.size() == 0) return 0;

        int length = height.size();
        vector<int> leftMax(length);
        vector<int> rightMax(length);
        leftMax[0] = height[0];
        rightMax[length-1] = height[length-1];
        int total = 0;

        for(int i=1; i<length; ++i) leftMax[i] = max(leftMax[i-1], height[i]);

        for(int i=length-2; i>=0; --i) rightMax[i] = max(rightMax[i+1], height[i]);

        for(int i=0; i<length; i++) total += min(leftMax[i], rightMax[i]) - height[i];

        return total;
    }
};

// Solution 2
// Space Complexity: O(1)
class Solution {
public:
    int trap(vector<int>& height) {
        if (height.empty()) return 0;

        int l = 0, r = height.size() - 1;
        int left_max = height[l], right_max = height[r];
        int total = 0;

        while (l < r) {
            if (left_max < right_max) {
                l++;
                left_max = max(left_max, height[l]);
                total += left_max - height[l];
            }
            else {
                r--;
                right_max = max(right_max, height[r]);
                total += right_max - height[r];
            }
        }

        return total;
    }
};