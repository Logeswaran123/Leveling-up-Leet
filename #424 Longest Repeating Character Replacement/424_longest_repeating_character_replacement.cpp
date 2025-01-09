/*

---
MEDIUM
424. Longest Repeating Character Replacement
---

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

*/

// Solution 1
// Sliding Window
class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> count;
        int res = 0;
        int l = 0;

        for (int r = 0; r < s.size(); ++r) {
            count[s[r]] = 1 + count[s[r]];

            while ((r - l + 1) - maxFrequency(count) > k) {
                count[s[l]] -= 1;
                l += 1;
            }
            res = max(res, r - l + 1);
        }

        return res;
    }

private:
    int maxFrequency(unordered_map<char, int>& count) {
        int maxFreq = 0;
        for (auto& [key, value] : count) {
            maxFreq = max(maxFreq, value);
        }
        return maxFreq;
    }
};


// Solution 2
// Sliding Window Optimal
class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> count;
        int res = 0;
        int l = 0;

        int max_freq = 0;
        for (int r = 0; r < s.size(); ++r) {
            count[s[r]] = 1 + count[s[r]];
            max_freq = max(max_freq, count[s[r]]);

            while ((r - l + 1) - max_freq > k) {
                count[s[l]] -= 1;
                l += 1;
            }
            res = max(res, r - l + 1);
        }

        return res;
    }
};