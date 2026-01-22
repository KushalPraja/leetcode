 struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        
        ListNode* new_head = new ListNode();
        ListNode* curr = new_head;

        while (list1 != nullptr and list2 != nullptr){
            if (list1-> val <= list2-> val){
                curr -> next = new ListNode(list1-> val);
                list1 = list1 -> next;
                curr = curr -> next;
            }

            else if (list1 -> val > list2 -> val){
                curr -> next = new ListNode(list2-> val);
                list2 = list2 -> next;
                curr = curr -> next;
            }
        }

        if (list1 != nullptr){
            curr -> next = list1;
        }
        
        if (list2 != nullptr){
            curr -> next = list2;
        }

        return new_head -> next;
        
    }
};

