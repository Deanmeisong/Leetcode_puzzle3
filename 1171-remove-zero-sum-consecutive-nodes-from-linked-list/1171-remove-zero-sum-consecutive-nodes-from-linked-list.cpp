/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeZeroSumSublists(ListNode* head) {
        ListNode* dummy = new ListNode(0, head);
        unordered_map<int, ListNode*> Map;
        int s = 0;
        ListNode* cur = dummy;
        while(cur) {
            s += cur->val;
            Map[s] = cur;
            cur = cur->next;
        }
        cur = dummy;
        s = 0;
        while(cur) {
            s += cur->val;
            cur->next = Map[s]->next;
            cur = cur->next;
        }
        
        return dummy->next;
    }
};