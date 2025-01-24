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
        if (root == nullptr){
            return ret;      
        }
        queue<TreeNode*> q;
        q.push(root);
        int curr_max = pow(-10,5); //pow(base,exp) 
        int level = 1;
        while(!q.empty()){
            int tot = 0;
           int n = q.size();
            for( int i = 0; i<n;i++){
                TreeNode* curr = q.front();
                q.pop();
                if (curr != nullptr){
                    tot+= curr->val;
                    if(curr->left != nullptr){
                        q.push(curr->left);
                    }
                    if(curr->right != nullptr){
                        q.push(curr->right);
                    }
                }
                std:: cout<< "curr->val: " << curr->val<< " tot: "<< tot<<"\n";
            }
            //////////////////////////////////
            if (curr_max < tot){
                ret = level;
                curr_max = tot;
            }
            level+=1;
        }
    return ret;
    }
};