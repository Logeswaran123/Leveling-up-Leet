"""

---
MEDIUM
207. Course Schedule
---

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

"""

## Solution 1
# Good to look at this problem.
#
# The problem asks whether it's possible to finish all courses given their prerequisites.
# We can represent the courses as nodes in a graph, where an edge from node A to node B means course A depends on course B.
# The problem becomes determining if there are any cycles in the dependency graph.
# If a cycle exists, we can't complete all the courses, because a course would depend on itself eventually.
# If no cycle exists, we can complete all courses.
#
# Example 1:
# Suppose there are 2 courses: 0 and 1. 
# The prerequisites are: [[1, 0]], which means course 1 depends on course 0.
#
# The graph would look like this:
# 0 --> 1
#
# The logic:
# 1. We first build an adjacency list `prereq_map` from the input prerequisites.
#    prereq_map = {0: [], 1: [0]}
#    This tells us course 0 has no prerequisites, while course 1 requires course 0.
#
# 2. The algorithm uses Depth-First Search (DFS) to check for cycles.
#    It keeps track of visited nodes to detect cycles.
#    If we revisit a node that is already in the current DFS path, it means there's a cycle.
#
#    The DFS function works as follows:
#    - If the course is in `visited`, it means we're in a cycle, so return False.
#    - If the course has no prerequisites (`prereq_map[course] == []`), return True.
#    - Add the course to `visited`, then recursively call DFS on its prerequisites.
#    - After visiting all its prerequisites successfully, remove the course from `visited`
#      and mark it as having no prerequisites by setting `prereq_map[course] = []`.
#
# 3. For each course, we run DFS. If any DFS call detects a cycle, return False.
#    If no cycles are found, return True.
#
# In this example:
# - Start DFS for course 0: it has no prerequisites, so it returns True.
# - Start DFS for course 1: it depends on course 0, so we call DFS on course 0, which returns True.
#   Therefore, course 1 can also be finished, so we return True for course 1.
# Since no cycles are detected, the function returns True, meaning all courses can be finished.
#
###
#
# Example 2: [[0, 1], [1, 2], [1, 3], [2, 4]]
# This means:
# - Course 0 depends on course 1.
# - Course 1 depends on course 2 and course 3.
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
# 2. For each course, run DFS:
#    - Start with course 0: 
#      It depends on course 1, so call DFS on course 1.
#    - Course 1 depends on courses 2 and 3. Call DFS on course 2:
#      - Course 2 depends on course 4. Call DFS on course 4.
#      - Course 4 has no prerequisites, so return True for course 4.
#      - Now, course 2 is also done, so return True for course 2.
#    - Next, check course 3. It has no prerequisites, so return True for course 3.
#    - Now, all prerequisites of course 1 are completed, so return True for course 1.
#    - Finally, course 0 is completed since its only prerequisite (course 1) is done.
# 3. No cycles are found, so the function returns True, meaning all courses can be finished.
#
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = {i:[] for i in range(numCourses)}
        visited = set()

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        def dfs(course):
            if course in visited:
                return False
            if prereq_map[course] == []:
                return True

            visited.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            prereq_map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True