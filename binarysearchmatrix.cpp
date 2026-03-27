#include <vector>

using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>&matrix, int target) {
        int left = 0;
        int right = matrix.size() -1; // number of column 

        while (left <= right){
            int mid = (left + right)/2;
            if (target < matrix[mid][0]){
                right = mid - 1;
            }
            else if (matrix[mid][matrix[0].size()-1] < target){
                left = mid + 1;
            }
            else {
                break;
            }
        }

        int mid = (left + right) / 2;
        left = 0;
        right = matrix[0].size() -1;
        while (left <= right){
            int idx_mid = (left + right)/2;
            if (matrix[mid][idx_mid] == target){
                return true;
            }
            else if (target > matrix[mid][idx_mid]){
                left = idx_mid + 1;
            }
            else{
                right = idx_mid - 1;
            }
        }
        return false;
    }
};
