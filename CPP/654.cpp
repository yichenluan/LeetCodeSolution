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
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {

        auto root = treeHelper(nums.begin(), nums.end());

        return root;
    }


    TreeNode* treeHelper(vector<int>::iterator begin, vector<int>::iterator end) {
        if (begin >= end) {
            return nullptr;
        }
        auto max_iter = begin;
        auto curr_begin = begin;
        int max_num = *max_iter;
        for (; curr_begin != end; ++curr_begin) {
            if (*curr_begin > max_num) {
                max_iter = curr_begin;
                max_num = *curr_begin;
            }
        }

        auto root_node = new TreeNode(max_num);
        root_node->left = treeHelper(begin, max_iter);
        root_node->right = treeHelper(max_iter + 1, end);

        return root_node;
    }
};
