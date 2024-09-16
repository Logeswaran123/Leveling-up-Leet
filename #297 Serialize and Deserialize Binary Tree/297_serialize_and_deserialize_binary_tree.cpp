/*

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

*/

// Solution 1
//
// Let's break down the logic using an example binary tree:
//
//        1
//       / \
//      2   3
//         / \
//        4   5
//
// When serialized, this tree will be converted into a string in a depth-first manner (pre-order traversal).
//
// **Serialize Method:**
// The `serialize` method converts the binary tree into a comma-separated string.
// It uses a helper function `dfs` to traverse the tree recursively in a pre-order manner (root -> left -> right).
// - For each node, it adds the node's value to the `res` list.
// - If a node is `nullptr`, it adds the string "N" to represent a null node.
// - The final result is a string of all values joined by commas.
//
// Let's go through the example tree step-by-step:
// 1. Start at the root (1). Add "1" to `res` and move to the left child (2).
// 2. Add "2" to `res`. Move to the left child of 2, which is `nullptr`, so add "N".
// 3. Move to the right child of 2, which is also `nullptr`, so add "N".
// 4. Return to the root (1) and move to the right child (3). Add "3" to `res`.
// 5. Move to the left child of 3 (4). Add "4" to `res`. Both children of 4 are `nullptr`, so add "N" twice.
// 6. Move to the right child of 3 (5). Add "5" to `res`. Both children of 5 are `nullptr`, so add "N" twice.
//
// The `res` list now contains: ["1", "2", "N", "N", "3", "4", "N", "N", "5", "N", "N"]
// This is joined into the string: "1,2,N,N,3,4,N,N,5,N,N"
//
// **Deserialize Method:**
// The `deserialize` method reconstructs the binary tree from the serialized string.
// It splits the string into a list of values and uses a helper function `dfs` to construct the tree recursively.
// - It uses an index `index` to keep track of the current position in the list.
// - If the current value is "N", it means the node is `nullptr`, so it returns `nullptr` and moves to the next value.
// - Otherwise, it creates a `TreeNode` with the current value and recursively builds its left and right children.
//
// For the example string "1,2,N,N,3,4,N,N,5,N,N":
// 1. Start with the first value "1". Create a root node with value 1. Move to the next value.
// 2. The next value is "2". Create a left child node with value 2. Move to the next value.
// 3. The next value is "N". This means the left child of 2 is `nullptr`. Move to the next value.
// 4. The next value is "N". This means the right child of 2 is `nullptr`. Return to the root.
// 5. The next value is "3". Create a right child node with value 3. Move to the next value.
// 6. The next value is "4". Create a left child node with value 4. Move to the next two values, both "N", which means both children of 4 are `nullptr`.
// 7. The next value is "5". Create a right child node with value 5. Move to the next two values, both "N", which means both children of 5 are `nullptr`.
//
// This reconstructs the original tree structure:
//        1
//       / \
//      2   3
//         / \
//        4   5
//
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
private:
    vector<string> split(const string &s, char delim) {
        vector<string> list;
        stringstream ss(s);
        string item;
        while (getline(ss, item, delim)) {
            list.push_back(item);
        }
        return list;
    }

    string join(const vector<string> &v, const string &delim) {
        ostringstream s;
        for (const auto &i : v) {
            if (&i != &v[0]) s << delim;    // Avoid adding delimiter before the first element
            s << i;
        }
        return s.str();
    }

    void dfs_serialize(TreeNode* node, vector<string>& res) {
        if (!node) {
            res.push_back("N");
            return;
        }
        res.push_back(to_string(node->val));
        dfs_serialize(node->left, res);
        dfs_serialize(node->right, res);
    }

    TreeNode* dfs_deserialize(vector<string>& values, int& i) {
        if (values[i] == "N") {
            i++;
            return NULL;
        }
        TreeNode* node = new TreeNode(stoi(values[i]));
        i++;
        node->left = dfs_deserialize(values, i);
        node->right = dfs_deserialize(values, i);
        return node;
    }

public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        vector<string> res;
        dfs_serialize(root, res);
        return join(res, ",");
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        vector<string> values = split(data, ',');
        int i = 0;  // Iterator for values list
        return dfs_deserialize(values, i);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));


// Solution 2
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) return "N"; // If tree is empty, return "N"

        string result;
        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();

            if (node) {
                result += to_string(node->val) + ","; // Add node value to string
                q.push(node->left);
                q.push(node->right);
            } else {
                result += "N,"; // Add "N" for null nodes
            }
        }

        // Remove trailing comma
        if (!result.empty()) result.pop_back();

        return result;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data == "N") return nullptr; // If input is "N", return empty tree

        stringstream ss(data);
        string token;
        getline(ss, token, ',');
        
        TreeNode* root = new TreeNode(stoi(token));
        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();

            // Process left child
            if (getline(ss, token, ',')) {
                if (token != "N") {
                    node->left = new TreeNode(stoi(token));
                    q.push(node->left);
                }
            }

            // Process right child
            if (getline(ss, token, ',')) {
                if (token != "N") {
                    node->right = new TreeNode(stoi(token));
                    q.push(node->right);
                }
            }
        }

        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));