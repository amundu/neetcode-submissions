# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []

        def dfs(root: Optional[TreeNode]) -> None:
            if not root: return
            nonlocal heap
            dfs(root.left)
            dfs(root.right)
            heapq.heappush(heap, root.val)
        dfs(root)
        for i in range(1, k):
            heapq.heappop(heap) 
        return heapq.heappop(heap)
        
