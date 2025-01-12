/*

---
MEDIUM
567. Permutation in String
---

Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.


*/

// Solution 1
// Sliding Window
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.length() > s2.length()) return false;

        vector<int> s1_count(26, 0), s2_count(26, 0);
        for (int i = 0; i < s1.length(); i++) {
            s1_count[s1[i] - 'a']++;
            s2_count[s2[i] - 'a']++;
        }

        int matches = 0;
        for (int i = 0; i < 26; i++) {
            if (s1_count[i] == s2_count[i]) {
                matches++;
            }
        }

        int l = 0;
        for (int r = s1.length(); r < s2.length(); r++) {
            if (matches == 26) {
                return true;
            }

            // Add new character to the window
            int idx = s2[r] - 'a';
            s2_count[idx]++;
            if (s1_count[idx] == s2_count[idx]) {
                matches++;
            } else if (s1_count[idx] + 1 == s2_count[idx]) {
                matches--;
            }

            // Remove old character from the window
            idx = s2[l] - 'a';
            s2_count[idx]--;
            if (s1_count[idx] == s2_count[idx]) {
                matches++;
            } else if (s1_count[idx] - 1 == s2_count[idx]) {
                matches--;
            }
            l++;
        }

        return matches == 26;
    }
};