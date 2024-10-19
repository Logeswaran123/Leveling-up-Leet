"""

---
MEDIUM
139. Word Break
---

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

"""

## Solution 1
#
# Example:
# s = "leetcode", wordDict = ["leet", "code"]
# We need to check if the string `s` can be segmented into words present in the word dictionary.
# Using dynamic programming, we build a table `dp` where dp[i] represents whether s[i:] can be segmented.
#
# Step-by-step explanation:
#
# 1. Initialize a dp array with size len(s) + 1 and set all values to False.
# dp = [False] * (len(s) + 1)
# The extra space at dp[len(s)] represents the end of the string and is set to True because an empty string is considered valid.
# dp[len(s)] = True
# For our example: s = "leetcode", len(s) = 8, so initially dp will be:
# dp = [False, False, False, False, False, False, False, False, True]
#
# 2. Now, we iterate backwards over the string `s`, starting from the last character and moving to the first.
# The goal is to check if any word in wordDict matches a substring starting at position `i`.
# If such a match is found and the remaining part of the string (after this word) can be segmented (i.e., dp[i + len(w)] is True), 
# then we set dp[i] = True.
#
# Let's walk through the example:
#
# i = 7 (last character "e"):
#  - Check each word in wordDict:
#    - "leet": doesn't match, continue.
#    - "code": doesn't match, continue.
#  - No match found, so dp[7] = False.
#
# i = 6:
#  - Check each word in wordDict:
#    - "leet": doesn't match.
#    - "code": doesn't match.
#  - No match found, dp[6] = False.
#
# i = 5:
#  - Same logic, no match found, dp[5] = False.
#
# i = 4:
#  - Check each word in wordDict:
#    - "leet": doesn't match.
#    - "code": Match found for s[4:8] == "code".
#    - Since dp[8] is True (base case), set dp[4] = True.
# dp = [False, False, False, False, True, False, False, False, True]
#
# i = 3:
#  - No match found, dp[3] = False.
#
# i = 2:
#  - No match found, dp[2] = False.
#
# i = 1:
#  - No match found, dp[1] = False.
#
# i = 0:
#  - Check each word in wordDict:
#    - "leet": Match found for s[0:4] == "leet".
#    - Since dp[4] is True, set dp[0] = True.
# dp = [True, False, False, False, True, False, False, False, True]
#
# 3. Finally, return dp[0], which tells whether the entire string can be segmented.
# In this case, dp[0] = True, meaning "leetcode" can be segmented as "leet" + "code".
#
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # Init
        dp[len(s)] = True   # Base case

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]