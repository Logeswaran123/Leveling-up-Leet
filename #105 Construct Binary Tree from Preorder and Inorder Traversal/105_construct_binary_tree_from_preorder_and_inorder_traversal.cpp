/*

---
MEDIUM
105. Construct Binary Tree from Preorder and Inorder Traversal
---

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

*/

// Solution 1
/**
 * Logic Explanation:
 * 
 * Example: preorder = [1, 2, 3, 4], inorder = [2, 1, 3, 4]
 * 
 * 1. The first element of the preorder vector is 1, which is the root of the tree.
 *    - Create a new TreeNode with value 1.
 * 
 * 2. Find the index of 1 in the inorder vector. Here, inorder = [2, 1, 3, 4], so the index of 1 is 1.
 *    - This splits the inorder vector into two parts:
 *      - Left subtree's inorder: [2] (elements before the root's index)
 *      - Right subtree's inorder: [3, 4] (elements after the root's index)
 * 
 * 3. The left subtree's preorder is obtained by taking the next 'mid' elements (from 1 to index of 1) from preorder:
 *    - Left subtree's preorder: [2]
 *    - The remaining elements form the right subtree's preorder: [3, 4]
 * 
 * 4. Recursively build the left subtree:
 *    - preorder = [2], inorder = [2]
 *    - Root of this subtree is 2. Since there are no more elements, both its left and right children will be null.
 * 
 * 5. Recursively build the right subtree:
 *    - preorder = [3, 4], inorder = [3, 4]
 *    - The root is 3 (first element of preorder). The index of 3 in inorder is 0.
 *    - This splits the inorder into:
 *      - Left subtree's inorder: [] (no elements)
 *      - Right subtree's inorder: [4]
 *    - Left subtree of 3 will be null (no elements).
 *    - Right subtree's preorder = [4], inorder = [4]:
 *      - Root is 4. Both left and right children will be null.
 * 
 * 6. The final tree structure:
 *         1
 *        / \
 *       2   3
 *            \
 *             4
 *
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.empty() || inorder.empty()) {
            return nullptr;
        }

        TreeNode* root = new TreeNode(preorder[0]);
        auto it = find(inorder.begin(), inorder.end(), preorder[0]);
        int mid = distance(inorder.begin(), it);
        
        vector<int> left_preorder(preorder.begin() + 1, preorder.begin() + mid + 1);
        vector<int> left_inorder(inorder.begin(), inorder.begin() + mid);
        vector<int> right_preorder(preorder.begin() + mid + 1, preorder.end());
        vector<int> right_inorder(inorder.begin() + mid + 1, inorder.end());

        root->left = buildTree(left_preorder, left_inorder);
        root->right = buildTree(right_preorder, right_inorder);
        
        return root;
    }
};