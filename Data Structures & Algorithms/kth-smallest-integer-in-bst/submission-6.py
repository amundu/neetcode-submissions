# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            nonlocal k
            if not root:
                return
            left = dfs(root.left)
            if left:
                return left
            if k == 1:
                return root.val
            k -= 1
            return dfs(root.right)
        return dfs(root)