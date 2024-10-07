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
    bool twoSumBSTs(TreeNode* root1, TreeNode* root2, int target) {
        vector<int> nums[2];
        function<void(TreeNode*, int)> inorder = [&](TreeNode* root, int i) {
            if(!root) return;
            inorder(root->left, i);
            nums[i].push_back(root->val);
            inorder(root->right, i);
        };
        inorder(root1, 0);
        inorder(root2, 1);
        int sum = 0;
        int i = 0, j = nums[1].size()-1;
        while(i < nums[0].size() && j >= 0) {
            sum = nums[0][i]+nums[1][j];
            if(sum == target) return true;
            if(sum < target) ++i;
            else --j;
        }
        return false;
    }
};