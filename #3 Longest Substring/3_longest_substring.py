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
        charset = set()
        window_left, longest_length = 0, 0
        for window_right in range(len(s)):
            while s[window_right] in charset:
                charset.remove(s[window_left])
                window_left += 1  
            charset.add(s[window_right])
            longest_length = max(longest_length, window_right - window_left + 1)
        return longest_length 