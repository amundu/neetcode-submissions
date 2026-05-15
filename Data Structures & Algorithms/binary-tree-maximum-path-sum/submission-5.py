# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_path = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> int:
            if not root: 
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            left = left if left > 0 else 0
            right = right if right > 0 else 0
            self.max_path = max(self.max_path, root.val + left + right)

            return root.val + max(left, right)
        dfs(root)
        return self.max_path