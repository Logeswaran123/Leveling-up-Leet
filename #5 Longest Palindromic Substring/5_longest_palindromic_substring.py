"""

---
MEDIUM
5. Longest Palindromic Substring
---

Given a string s, return the longest 
palindromic substring in s.
 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.


Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

"""

## Solution 1
class Solution:
    def palindrome(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    def longestPalindrome(self, s: str) -> str:
        longest_sub_s = ''
        for i in range(len(s)):
            s1 = self.palindrome(s, i, i) # For odd len substring
            s2 = self.palindrome(s, i, i+1) # For even len substring
            print(s1, s2)
            longest_sub_s = max([longest_sub_s, s1, s2], key=len)
        return longest_sub_s
