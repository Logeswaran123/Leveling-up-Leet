/*

---
MEDIUM
128. Longest Consecutive Sequence
---

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109


*/

// Solution 1
/*
Logic Explanation:

Input Array: [1, 100, 2, 4, 3, 200]

Step 1: Convert to Set
- nums_set = {1, 100, 2, 3, 4, 200}

Step 2: Find Longest Consecutive Sequence

- Check 1:
  - 1 is the start of a sequence (0 not in set).
  - Sequence: 1 → 2 → 3 → 4
  - Length = 4

- Check 100:
  - 100 is the start of a sequence (99 not in set).
  - Sequence: 100
  - Length = 1

- Check 2:
  - 2 is not the start (1 is in set). Skip.

- Check 3:
  - 3 is not the start (2 is in set). Skip.

- Check 4:
  - 4 is not the start (3 is in set). Skip.

- Check 200:
  - 200 is the start of a sequence (199 not in set).
  - Sequence: 200
  - Length = 1

Final Answer:
- Longest consecutive sequence length = 4 (from 1 → 2 → 3 → 4)
*/
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> nums_set(nums.begin(), nums.end());
        int longest_seq = 0;

        for (int num: nums_set) {
            if (nums_set.find(num-1) == nums_set.end()) { // Check if left num is starting sequence
                int length = 1;
                while (nums_set.find(num+length) != nums_set.end()) length++; // Iterate all consecutive nums
                longest_seq = max(length, longest_seq);
            }
        }

        return longest_seq;
    }
};