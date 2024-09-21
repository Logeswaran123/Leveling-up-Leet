"""

---
MEDIUM
261. Graph Valid Tree
---

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true
Example 2:

Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

Output:
false
Note:

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2

"""

## Solution 1
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:   # Empty is considered as a tree
            return True

        adj = { i:[] for i in range(n) }

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(curr_node, prev_node):
            if curr_node in visited:    # Loop is detected
                return False

            visited.add(curr_node)

            for node in adj[curr_node]:
                if node == prev_node:   # Continue when previous node is an adjacent node
                    continue

                if not dfs(node, curr_node):
                    return False

            return True

        # Since 0th node has not previous node, we use -1.
        # Number of node must be equal to all the nodes in visited set for fully connected tree (i.e. no node is left unconnected).
        return dfs(0, -1) and n == len(visited)