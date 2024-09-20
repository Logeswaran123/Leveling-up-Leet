"""

---
MEDIUM
210. Course Schedule II
---

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.

"""

## Solution 1
# Topological Sort
# Similar to #207. Good to look at this problem.
#
# Example: [[0, 1], [1, 2], [1, 3], [2, 4]]
# This means:
# - Course 0 depends on course 1.
# - Course 1 depends on courses 2 and 3.
# - Course 2 depends on course 4.
#
# The graph looks like this:
# 0 --> 1 --> 2 --> 4
#       |
#       v
#       3
#
# The logic:
# 1. We first build the adjacency list `prereq_map` from the input prerequisites:
#    prereq_map = {0: [1], 1: [2, 3], 2: [4], 3: [], 4: []}
#    This tells us which courses depend on others.
#
# 2. Use DFS to determine the order in which courses can be finished:
#    - `visited` set keeps track of courses that are fully processed (completed).
#    - `cycle` set helps detect cycles during the DFS traversal (a cycle means a course depends on itself directly or indirectly).
#    - `output` list stores the courses in reverse order (we process a course after all its prerequisites).
#
#    The DFS function works as follows:
#    - If a course is in `cycle`, it means we have a cycle, so return False (no valid course order).
#    - If a course is in `visited`, it means it's already been processed, so return True (no need to process again).
#    - Add the course to `cycle` to mark that we're currently processing it.
#    - For each prerequisite of the course, call DFS on it.
#    - After processing all prerequisites, remove the course from `cycle`, add it to `visited`, and append it to `output`.
#
# 3. Start DFS for each course:
#    - Start with course 0: 
#      Course 0 depends on course 1, so call DFS on course 1.
#    - Course 1 depends on courses 2 and 3. Start with course 2:
#      - Course 2 depends on course 4, so call DFS on course 4.
#      - Course 4 has no prerequisites, so return True and add it to `visited` and `output`.
#      - Course 2 is now processed since its prerequisite (course 4) is done, so return True and add course 2 to `output`.
#    - Now, check course 3:
#      - Course 3 has no prerequisites, so return True and add it to `visited` and `output`.
#    - Since all prerequisites of course 1 are completed, return True and add course 1 to `output`.
#    - Finally, course 0 can be completed since course 1 is done, so add course 0 to `output`.
#
# 4. The output list at this point is [4, 2, 3, 1, 0].
#
# 5. If a cycle is detected at any point, return an empty list.
#
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {i:[] for i in range(numCourses)}
        visited, cycle = set(), set()
        output = []

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False

            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return output