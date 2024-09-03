"""

---
MEDIUM
49. Group Anagrams
---

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


"""

## Solution 1
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> group;

        for (auto& s: strs) {
            vector<int> count(26, 0);
            for (char& c: s) {
                count[c-'a']++;
            }

            string key;
            for (int i: count) {
                key += "#" + to_string(i);
            }

            group[key].push_back(s);
        }

        vector<vector<string>> result;
        for (auto& g: group) {
            result.push_back(move(g.second));
        }

        return result;
    }
};


## Solution 2
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        unordered_map<string, vector<string>> group;

        for (auto& s: strs) {
            auto sorted = s;
            sort(sorted.begin(), sorted.end());
            group[sorted].push_back(move(s));
        }

        for (auto& g: group) {
            result.push_back(move(g.second));
        }

        return result;
    }
};