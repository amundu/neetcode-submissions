/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        HashMap<Node, Node> ogToCopy = new HashMap();
        ogToCopy.put(null, null);

        Node curr = head;

        while (curr != null){
            ogToCopy.put(curr, new Node(curr.val));
            curr = curr.next;
        }

        curr = head;

        while (curr != null){
            ogToCopy.get(curr).random = ogToCopy.get(curr.random);
            ogToCopy.get(curr).next = ogToCopy.get(curr.next);
            curr = curr.next;
        }

        return ogToCopy.get(head);
    }
}
