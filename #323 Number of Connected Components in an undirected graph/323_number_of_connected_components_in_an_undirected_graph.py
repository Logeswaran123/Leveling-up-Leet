"""

---
MEDIUM
323. Number of Connected Components in an undirected graph
---

There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Example 1:

Input:
n=3
edges=[[0,1], [0,2]]

Output:
1
Example 2:

Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]

Output:
2
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2

"""

## Solution 1
# Similar to #684
# Union Find with Path Compression. Good to look at this problem.
# Kinda confusing at first glance.
#
# Example:
# n = 5, edges = [[0, 1], [1, 2], [3, 4]]
# Initially, each node is its own component: {0}, {1}, {2}, {3}, {4}.
#
# The undirected graph looks like this:
# 0 -- 1     3 -- 4
#      | 
#      2
#
# Step 1: Union(0, 1)
# Find parent of 0 -> 0
# Find parent of 1 -> 1
# Union 0 and 1 -> {0, 1}, now we have {0, 1}, {2}, {3}, {4}
# Components = 4
#
# Step 2: Union(1, 2)
# Find parent of 1 -> 0 (1 points to 0 due to path compression)
# Find parent of 2 -> 2
# Union 1 and 2 -> {0, 1, 2}, now we have {0, 1, 2}, {3}, {4}
# Components = 3
#
# Step 3: Union(3, 4)
# Find parent of 3 -> 3
# Find parent of 4 -> 4
# Union 3 and 4 -> {3, 4}, now we have {0, 1, 2}, {3, 4}
# Components = 2
#
# Final result: 2 components.
#
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        # Find the root parent of a node with path compression
        def find_parent(n):
            res = n

            # Traverse up the tree until you find root parent (a node that is its own parent)
            while res != parent[res]:
                parent[res] = parent[parent[res]]    # Path compression: point current node directly to its grandparent
                res = parent[res]  # Set parent

            return res

        # Find Union between nodes
        def union(n1, n2):
            p1, p2 = find_parent(n1), find_parent(n2)

            # If they are already in same set (same parent), no union is made
            if p1 == p2:
                return 0

            # Otherwise, we union the two sets based on their ranks.
            # The tree with higher rank becomes parent of the other.
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]

            return 1

        res = n
        for n1, n2 in edges:    # For each edge, attempt to union the two nodes
            res -= union(n1, n2)

        return res