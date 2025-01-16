"""

---
MEDIUM
22. Generate Parentheses
---

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

"""

## Solution 1
## Stack and Recursion
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(num_open, num_close):
            if num_open == num_close == n:
                res.append("".join(stack))
                return

            if num_open < n:
                stack.append("(")
                backtrack(num_open + 1, num_close)
                stack.pop()
            if num_close < num_open:
                stack.append(")")
                backtrack(num_open, num_close + 1)
                stack.pop()

        backtrack(0, 0)
        return res