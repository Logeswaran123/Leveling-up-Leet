/*

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

*/

// Solution 1
// Stack and Recursion
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string current;

        function<void(int, int)> backtrack = [&](int num_open, int num_close) {
            if (num_open == n && num_close == n) {
                res.push_back(current);
                return;
            }

            if (num_open < n) {
                current.push_back('(');
                backtrack(num_open + 1, num_close);
                current.pop_back();
            }
            if (num_close < num_open) {
                current.push_back(')');
                backtrack(num_open, num_close + 1);
                current.pop_back();
            }
        };

        backtrack(0, 0);
        return res;
    }
};