/*

---
EASY
242. Valid Anagrams
---

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


*/

// Solution 1
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        unordered_map<char, int> track;
        for(int i=0; i<s.size(); i++) {
            track[s[i]]++;
            track[t[i]]--;
        }

        for (auto& it: track) {
            if (it.second != 0) return false;
        }
        return true;
    }
};


// Solution 2
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        int char_counter[26] = {0};
        for(int i=0; i<s.size(); i++) {
            char_counter[s[i] - 'a']++;
            char_counter[t[i] - 'a']--;
        }

        for (auto& count: char_counter) {
            if (count != 0) return false;
        }
        return true;
    }
};