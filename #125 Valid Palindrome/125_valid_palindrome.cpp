/*

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


*/

// Solution 1
class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size() - 1;

        while(l<=r) {
            if (!isalnum(s[l])) l++;
            else if (!isalnum(s[r])) r--;
            else {
                if (tolower(s[l]) != tolower(s[r])) return false;
                l++;
                r--;
            }
        }

        return true;
    }
};

// Solution 2
class Solution {
public:
    bool is_alphanum(char c) {
        if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')) return true;
        return false;
    }

    char to_lower(char c) {
        if (c >= 'a' && c <= 'z') return c;
        return c + ('a' - 'A');
    }

    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size() - 1;

        while(l<=r) {
            if (!is_alphanum(s[l])) l++;
            else if (!is_alphanum(s[r])) r--;
            else {
                if (to_lower(s[l]) != to_lower(s[r])) return false;
                l++;
                r--;
            }
        }

        return true;
    }
};
