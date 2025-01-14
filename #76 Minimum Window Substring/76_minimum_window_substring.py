"""

---
HARD
76. Minimum Window Substring
---

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?

"""

## Solution 1
## Sliding Window
#
# Example:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window in 's' that contains all characters in 't' is "BANC".
#
# Logic:
# 1. If 't' is empty, return an empty string (no characters to match).
# 2. Create a frequency count ('count_t') for characters in 't'.
# 3. Use a sliding window approach with two pointers 'l' (left) and 'r' (right).
#    - Expand the window by moving 'r' and update the frequency count in the 'window' dictionary.
#    - Track the number of characters in 't' that are satisfied in the current window ('have').
# 4. When all characters are satisfied ('have == need'), try to shrink the window from the left ('l') 
#    to find the smallest valid window:
#    - Update the result if the current window is smaller.
#    - Decrease the count of the character at 'l' in 'window' and reduce 'have' if it goes below the required count.
#    - Move 'l' to the right.
# 5. Return the substring corresponding to the smallest window, or an empty string if no such window exists.
#
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_t, window = {}, {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                    
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if res_len != float("infinity") else ""