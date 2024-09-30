"""

---
MEDIUM
684. Redundant Connection
---

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.

"""

## Solution 1
# Similar to #323. See #323 for explanation of the logic.
# Union Find with Path Compression. Good to look at this problem.
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        # Find the parent of a node with path compression
        def find_parent(n):
            res = n

            # Traverse up until you find root parent (a node that is its own parent)
            while res != parent[res]:
                parent[res] = parent[parent[res]]    # Path compression: point current node directly to its grandparent
                res = parent[res]  # Set parent

            return res

        # Find Union between nodes
        def union(n1, n2):
            p1, p2 = find_parent(n1), find_parent(n2)

            # If they are already in same set (same parent), no union is made
            if p1 == p2:
                return False

            # Otherwise, we union the two sets based on their ranks.
            # The node with higher rank becomes parent of the other.
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]

            return True

        for n1, n2 in edges:    # For each edge, attempt to union the two nodes
            if not union(n1, n2):
                return [n1, n2]