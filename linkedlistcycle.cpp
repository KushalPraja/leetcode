#include <vector>
#include <algorithm>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        
        ListNode* curr = head;
        std::vector<ListNode*> x {};
        while (curr != nullptr){
            auto it = std::find(x.begin(), x.end(), curr);
            if (it != x.end()){
                return true;
            }
            x.push_back(curr);
            curr = curr-> next;
        }
        return false;
    }
};
