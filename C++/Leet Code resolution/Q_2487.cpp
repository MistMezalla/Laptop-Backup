#include <bits/stdc++.h>
using namespace std;

// Definition for singly-linked list provided by LeetCode environment.
// struct ListNode {
//     int val;
//     ListNode *next;
//     ListNode() : val(0), next(nullptr) {}
//     ListNode(int x) : val(x), next(nullptr) {}
//     ListNode(int x, ListNode *next) : val(x), next(next) {}
// };

class Solution {
public:
    ListNode* removeNodes(ListNode* head) {
        if (!head)
            return nullptr;
            
        ListNode* curr = head;
        ListNode* prev = nullptr;

        // Reverse the linked list
        while (curr) {
            ListNode* nextNode = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextNode;
        }

        // Now prev is the head of the reversed list
        // if (!prev) return nullptr;

        curr = prev->next;
        prev->next = nullptr;

        while (curr) {
            ListNode* temp = curr->next;
            if (curr->val >= prev->val) {
                curr->next = prev;
                prev = curr;
            }
            curr = temp;
        }

        return prev;
    }
};
