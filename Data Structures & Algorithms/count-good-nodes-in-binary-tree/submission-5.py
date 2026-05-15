# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, max_value):
            nonlocal res
            if not root:
                return 
            res += int(max_value <= root.val)
            left = dfs(root.left, max(max_value, root.val))
            right = dfs(root.right, max(max_value, root.val))
            
        dfs(root, float('-inf'))
        return res