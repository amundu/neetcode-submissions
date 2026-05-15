# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_value):
            if not root:
                return 0
            left = dfs(root.left, max(max_value, root.val))
            right = dfs(root.right, max(max_value, root.val))
            return left + right + int(max_value <= root.val)
            
        return dfs(root, float('-inf'))