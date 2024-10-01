"""

---
HARD
127. Word Ladder
---

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.

"""

## Solution 1
# Similar to BFS. Easy to understand Logic.
#
# Example Explanation:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
#
# 1. We start with "hit". We create patterns like:
#     *it, h*t, hi*
#
# 2. From the pattern "h*t", we can move to "hot" (from the wordList). Now, add "hot" to the queue.
#
# 3. Now we move to the next word, "hot", and create patterns:
#     *ot, h*t, ho*
#    From pattern "*ot", we can move to "dot" and "lot".
#
# 4. We move to "dot" next, and from "*ot" we can move to "dog". We also process "lot" from the previous step.
#
# 5. Continue this process, building patterns and exploring neighbors. Eventually, we reach the word "cog".
#
# In this example, the shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", and the output will be 5.
#
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # Create a dictionary to hold all the intermediate patterns as keys and the list of words
        # that match these patterns as values. For example, "h*t" will be a pattern for "hit" and "hot".
        neighbors = collections.defaultdict(list)
        wordList.append(beginWord)

        # Build neighbors dictionary: for each word in wordList, for each letter position, 
        # replace the letter with '*' to create a pattern. Map the pattern to the word.
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbors[pattern].append(word)

        visited = set([beginWord])  # To track visited words and avoid cycles
        q = deque([beginWord])  # Queue to hold the words at the current level (breadth-first search)
        res = 1 # Transformation count

        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbor in neighbors[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
            res += 1

        # If the endWord is not reached, return 0
        return 0