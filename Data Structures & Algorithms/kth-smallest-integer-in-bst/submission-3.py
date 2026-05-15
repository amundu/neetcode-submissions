# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        visits = 0
        def dfs(root, n, k):
            nonlocal visits, res
            if not root:
                return
            left = dfs(root.left, n, k)
            visits += 1
            if visits == k:
                res = root.val
            right = dfs(root.right, left, k)
        dfs(root, 0, k)
        return res