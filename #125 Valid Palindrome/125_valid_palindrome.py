"""

---
EASY
125. Valid Palindrome
---

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.


"""

## Solution 1
# ord() is used to get the ASCII char in python
class Solution:
    def is_alphanum(self, c: str):
        if ((ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z')) or 
            (ord('0') <= ord(c) <= ord('9'))):
            return True
        return False

    def to_lower(self, c: str):
        return c.lower()

    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while(l<=r):
            if (not self.is_alphanum(s[l])): l+=1
            elif (not self.is_alphanum(s[r])): r-=1
            else:
                if (self.to_lower(s[l]) != self.to_lower(s[r])):
                    return False
                l+=1
                r-=1
        return True