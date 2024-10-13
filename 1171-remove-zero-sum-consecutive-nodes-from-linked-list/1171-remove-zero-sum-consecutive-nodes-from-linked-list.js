/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var removeZeroSumSublists = function(head) {
    const dummy = new ListNode(0, head);
    const last = new Map();
    let s = 0;

    // First pass: store the last occurrence of each prefix sum
    for (let cur = dummy; cur !== null; cur = cur.next) {
        s += cur.val;
        last.set(s, cur);
    }

    s = 0;

    // Second pass: connect nodes to skip zero-sum sublists
    for (let cur = dummy; cur !== null; cur = cur.next) {
        s += cur.val;
        cur.next = last.get(s).next;
    }

    return dummy.next;
};