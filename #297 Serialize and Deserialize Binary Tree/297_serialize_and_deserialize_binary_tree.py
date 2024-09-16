"""

---
HARD
297. Serialize and Deserialize Binary Tree
---

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000

"""

## Solution 1
##
# Let's break down the logic using an example binary tree:
#
#        1
#       / \
#      2   3
#         / \
#        4   5
#
# When serialized, this tree will be converted into a string in a depth-first manner (pre-order traversal).
#
# **Serialize Method:**
# The `serialize` method converts the binary tree into a comma-separated string.
# It uses a helper function `dfs` to traverse the tree recursively in a pre-order manner (root -> left -> right).
# - For each node, it adds the node's value to the `res` list.
# - If a node is `None`, it adds the string "N" to represent a null node.
# - The final result is a string of all values joined by commas.
#
# Let's go through the example tree step-by-step:
# 1. Start at the root (1). Add "1" to `res` and move to the left child (2).
# 2. Add "2" to `res`. Move to the left child of 2, which is `None`, so add "N".
# 3. Move to the right child of 2, which is also `None`, so add "N".
# 4. Return to the root (1) and move to the right child (3). Add "3" to `res`.
# 5. Move to the left child of 3 (4). Add "4" to `res`. Both children of 4 are `None`, so add "N" twice.
# 6. Move to the right child of 3 (5). Add "5" to `res`. Both children of 5 are `None`, so add "N" twice.
#
# The `res` list now contains: ["1", "2", "N", "N", "3", "4", "N", "N", "5", "N", "N"]
# This is joined into the string: "1,2,N,N,3,4,N,N,5,N,N"
#
# **Deserialize Method:**
# The `deserialize` method reconstructs the binary tree from the serialized string.
# It splits the string into a list of values and uses a helper function `dfs` to construct the tree recursively.
# - It uses an index `self.i` to keep track of the current position in the list.
# - If the current value is "N", it means the node is `None`, so it returns `None` and moves to the next value.
# - Otherwise, it creates a `TreeNode` with the current value and recursively builds its left and right children.
#
# For the example string "1,2,N,N,3,4,N,N,5,N,N":
# 1. Start with the first value "1". Create a root node with value 1. Move to the next value.
# 2. The next value is "2". Create a left child node with value 2. Move to the next value.
# 3. The next value is "N". This means the left child of 2 is `None`. Move to the next value.
# 4. The next value is "N". This means the right child of 2 is `None`. Return to the root.
# 5. The next value is "3". Create a right child node with value 3. Move to the next value.
# 6. The next value is "4". Create a left child node with value 4. Move to the next two values, both "N", which means both children of 4 are `None`.
# 7. The next value is "5". Create a right child node with value 5. Move to the next two values, both "N", which means both children of 5 are `None`.
#
# This reconstructs the original tree structure:
#        1
#       / \
#      2   3
#         / \
#        4   5
#
##
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        res = ",".join(res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(",")
        self.i = 0  # Iterator for values list

        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))