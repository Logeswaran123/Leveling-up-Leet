"""

---
EASY
20. Valid Parentheses
---

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""

## Solution 1
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0 or (s[0] in [")", "]", "}"]):
            return False

        tracker = []
        for char in s:
            if char in ["(", "[", "{"]:
                tracker.append(char)
                continue
            if len(tracker) == 0 and (char in [")", "]", "}"]):
                return False
            if len(tracker) > 0:
                if char == ")" and tracker[-1] == "(":
                    tracker.pop()
                elif char == "]" and tracker[-1] == "[":
                    tracker.pop()
                elif char == "}" and tracker[-1] == "{":
                    tracker.pop()
                else:
                    return False
        return len(tracker) == 0


## Solution 2
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0 or (s[0] in [")", "]", "}"]):
            return False

        dic = {'(':')', '[':']', '{':'}'}
        tracker = []
        for char in s:
            if char in dic:
                tracker.append(char)
            elif len(tracker) == 0 or dic[tracker.pop()] != char:
                return False
        return len(tracker) == 0