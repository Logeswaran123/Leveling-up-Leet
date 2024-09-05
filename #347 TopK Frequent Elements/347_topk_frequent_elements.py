"""

---
MEDIUM
347. TopK Frequent Elements
---

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


"""

## Solution 1
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<vector<int>> freq(nums.size() + 1);
        vector<int> res;

        for (int& num: nums) {
            count[num] += 1;
        }

        for (const auto& num: count) {
            freq[num.second].push_back(num.first);
        }

        for (int i=freq.size()-1; i>0; i--) {
            for (auto& num: freq[i]) {
                res.push_back(num);
                if (res.size() == k) return res;
            }
        }
        return res;
    }
};


## Solution 2
class Solution {
public:
    static bool func(pair<int, int> a, pair<int, int> b) {
        return a.second > b.second;
    }

    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<pair<int, int>> freq;
        vector<int> res;

        for (int& num: nums) {
            count[num]++;
        }

        for (const auto& num: count) {
            freq.push_back({num.first, num.second});
        }

        sort(freq.begin(), freq.end(), func);
        for (int i=0; i<k; i++) {
            res.push_back(freq[i].first);
        }
        return res;
    }
};