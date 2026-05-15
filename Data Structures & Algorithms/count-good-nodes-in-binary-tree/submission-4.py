# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_value):
            if not root: return 0
            return int(root.val >= max_value) + dfs(root.left, max(max_value, root.val)) + dfs(root.right, max(max_value, root.val))
            
        return dfs(root, float('-inf'))