
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))
        
        dummy = curr = ListNode()
        while min_heap:
            _, i = heapq.heappop(min_heap)
            node = lists[i]
            curr.next = node
            curr = curr.next
            lists[i] = node.next
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))
        return dummy.next