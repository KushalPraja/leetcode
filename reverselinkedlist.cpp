#include <iostream>

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  ListNode *reverseList(ListNode *head) {

    ListNode *curr = head;
    ListNode *prev = nullptr;

    while (curr != nullptr) {
      ListNode *next = curr->next;
      curr->next = prev;
      prev = curr;
      curr = next;
    }

    return prev;
  }
};

int main(){
  ListNode *head = new ListNode(5, new ListNode(6, new ListNode(7)));
  Solution x;
  ListNode *new_head = x.reverseList(head);

  while (new_head != nullptr) {
    std::cout << new_head -> val << std::endl;
    new_head = new_head->next;
  }
  return 0;
};
