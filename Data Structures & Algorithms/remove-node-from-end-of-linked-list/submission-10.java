/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode front = head;
        ListNode dummy = new ListNode();
        dummy.next = head;

        for (int i = 0; i < n; i++){
            front = front.next;
        }

        ListNode curr = dummy;
        while (front != null){
            curr = curr.next;
            front = front.next;
        }

        curr.next = curr.next.next;
        return dummy.next;
    }
}
