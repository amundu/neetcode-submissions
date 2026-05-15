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
    public void reorderList(ListNode head) {
        if (head == null) return;
        ListNode fast = head.next;
        ListNode slow = head;

        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }

        // Reverse half
        ListNode prev = slow;
        slow = slow.next;
        prev.next = null;
        prev = null;
        while (slow != null){
            System.out.println(slow.val);
            ListNode temp = slow.next;
            slow.next = prev;
            prev = slow;
            slow = temp;
        }
        ListNode tail = prev;
        ListNode curr = head;

        while (tail != null) {
            System.out.println(curr.val + " " + tail.val);
            ListNode currNext = curr.next;
            ListNode tailNext = tail.next;
            curr.next = tail;
            tail.next = currNext;
            curr = currNext;
            tail = tailNext;
        }
    }
}
