"""

---
MEDIUM
3. Longest Substring Without Repeating Characters
---

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""

## Solution 1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_split = list(s)
        result = 0
        for i, s1 in enumerate(s_split):
            max_val = 1
            tracker = []
            for s2 in s_split[i+1:]:
                if s1 != s2 and s2 not in tracker:
                    tracker.append(s2)
                    max_val += 1
                else:
                    break
            result = max_val if max_val > result else result
        return result


## Solution 2
### Sliding Window method
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
        return res


## Solution 3
### Sliding Window Optimized
# This function finds the length of the longest substring in a given string s 
# that contains only unique characters. 
# It uses a sliding window approach with two pointers (l and r) and a dictionary (last_seen_idx) 
# to keep track of the last seen indices of characters.
# The steps are:
# 1. Expand the right pointer (r) to iterate through the string.
# 2. If a duplicate character is found, move the left pointer (l) to exclude the previous occurrence.
#       Specifically, set l to the maximum of:
#           The next index after the last occurrence of s[r] (last_seen_idx[s[r]] + 1).
#           The current l, to ensure it doesn't move backward.
# 3. Update the dictionary with the current character's index.
# 4. Calculate the current substring length and update the result (res) if it's larger.
# 5. Return the maximum length of a substring with unique characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen_idx = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            if s[r] in last_seen_idx:
                l = max(last_seen_idx[s[r]] + 1, l)
            last_seen_idx[s[r]] = r
            res = max(res, r - l + 1)
        return res