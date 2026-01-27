#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        
        vector<int> x{};
        vector<vector<int>> res{};
        generate(nums, {}, res,0);
        return res;

    }

    void generate(vector<int> nums, vector<int> path, vector<vector<int>>&res, int start){

        res.push_back(path);
        
        if (path.size() == nums.size()){
            return;
        }

        for (int i = start; i < nums.size(); i++){
            auto it = std::find(path.begin(), path.end(), nums[i]);
            if (it == path.end()){
                path.push_back(nums[i]);
                generate(nums, path, res, i + 1);
                path.pop_back();
            }
        }
    }
};

