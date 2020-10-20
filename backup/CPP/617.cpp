/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (t1 == NULL && t2 == NULL) {
            return NULL;
        }

        if (t1 == NULL || t2 == NULL) {
            return (t1 == NULL)? t2: t1;
        }

        TreeNode *new_p = new TreeNode(t1->val + t2->val);
        new_p->left = mergeTrees(t1->left, t2->left);
        new_p->right = mergeTrees(t1->right, t2->right);
        return new_p;
    }
};
