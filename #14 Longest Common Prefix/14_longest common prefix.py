"""

---
EASY
14. Longest Common Prefix
---

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

"""

## Solution 1
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        count_matching = 0
        minimum, maximum = min(strs), max(strs)
        for i in range(len(minimum)):
            if minimum[i] != maximum[i]:
                break
            else:
                count_matching += 1
        return minimum[:count_matching]