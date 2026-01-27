#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {

        unordered_map<int, int>levels;
        dfs(root, levels, 0);
        vector<int> res;

        for (auto i: levels){
            res.push_back(i.second);
        }
        reverse(res.begin(), res.end());
        return res;

    }

    void dfs(TreeNode* root, unordered_map<int, int> &levels, int level){
        if (root == nullptr){
            return;
        }
        
        if (levels[level] == 0){
            levels[level]= root -> val;
        }
        
        dfs(root-> right, levels, level + 1);
        dfs(root-> left, levels, level + 1);
        
    }
};
