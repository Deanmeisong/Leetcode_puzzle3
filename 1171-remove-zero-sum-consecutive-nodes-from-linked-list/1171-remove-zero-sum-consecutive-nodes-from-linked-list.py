# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        prefix_sum_map = {}
        s = 0
        cur = dummy

        # First pass to calculate prefix sums and store nodes in map
        while cur:
            s += cur.val
            prefix_sum_map[s] = cur
            cur = cur.next

        # Second pass to remove nodes part of zero-sum sublists
        cur = dummy
        s = 0
        while cur:
            s += cur.val
            cur.next = prefix_sum_map[s].next
            cur = cur.next

        return dummy.next