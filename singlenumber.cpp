#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {

        unordered_map<int,int> x = {};
        for (auto a: nums){
            x[a]++;
        }
        

        for (auto i: x){
            if(i.second == 1){
              return i.first;
            }
        }
        return -1;
    }
};

int main(){
  Solution sol;
  vector<int>nums = {2,2,1};
  int x = sol.singleNumber(nums);
}

