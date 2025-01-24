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
#include <queue>
#include <cmath>
class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        int ret = 0;
        int level = 1;
        int curr_max = -pow(10,5);
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            int tot  =0;
            int n = q.size();
            for(int i = 0; i<n; i++){
                TreeNode* curr = q.front();
                q.pop();
                if (curr != nullptr){
                    tot +=curr->val;
                    if(curr->left != nullptr){
                        q.push(curr->left);
                    }
                    if(curr->right != nullptr){
                        q.push(curr->right);
                    }
                }
            }
            if (curr_max<tot){
                ret = level;
                curr_max = tot;
            }
            level++;

        }

        return ret;
    }
};