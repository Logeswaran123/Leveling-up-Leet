"""

---
MEDIUM
133. Clone Graph
---

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
 

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.

"""

## Solution 1
#
# This function `cloneGraph` creates a deep copy of an undirected graph using Depth-First Search (DFS).
# The graph is represented using Node objects, each having a `val` and a list of `neighbors`.
#
# Steps:
# 1. If the input `node` is `None`, return `None` because there's nothing to clone.
# 2. Create an `unordered_map` (in C++, `unordered_map` is used, similar to a Python dictionary) to map each original node to its cloned node.
# 3. Define a DFS function using a lambda:
#    - If the current node (`node_1`) is already in the map, it means it has been cloned before, so return the cloned node to avoid duplicates.
#    - Otherwise, create a new node (`new_node`) with the same value as `node_1` and store it in the map to track that this node is now cloned.
#    - Iterate through each neighbor of the current node (`node_1`):
#        - Recursively call the DFS function for each neighbor and add the returned (cloned) neighbor nodes to `new_node`'s `neighbors` list.
#    - Return the newly created node (`new_node`).
# 4. Start the DFS from the input `node` and return the cloned graph.
#
# Example:
# Let's say we have a graph with the following adjacency list:
# adjList = [[2], [1, 3], [2]]
#
# Visual representation:
# Node 1 is connected to Node 2
# Node 2 is connected to Node 1 and Node 3
# Node 3 is connected to Node 2
#
# Process:
# - Start DFS from Node 1:
#   - Create a new node for Node 1 and store it in the map.
#   - Visit its neighbor, Node 2:
#     - Create a new node for Node 2 and store it in the map.
#     - Visit Node 2's neighbors:
#       - First neighbor is Node 1, which is already cloned (exists in the map), so return the cloned Node 1.
#       - Second neighbor is Node 3:
#         - Create a new node for Node 3 and store it in the map.
#         - Visit Node 3's neighbors:
#           - Neighbor is Node 2, which is already cloned, so return the cloned Node 2.
# - This process continues until all nodes and their neighbors are cloned.
# - The function returns the cloned Node 1, which is the entry point to the entire cloned graph.
#
# Output:
# The output is a deep copy of the input graph. For the given adjacency list [[2], [1, 3], [2]], 
# the cloned graph will have the same structure with a new set of nodes.
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        map = {}

        def dfs(node):
            if node in map:
                return map[node]

            new_node = Node(node.val)
            map[node] = new_node
            for n in node.neighbors:
                new_node.neighbors.append(dfs(n))

            return new_node

        return dfs(node)