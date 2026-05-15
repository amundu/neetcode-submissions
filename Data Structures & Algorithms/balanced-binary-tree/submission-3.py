# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        return self.dfs(root)[0]
        
    def dfs(self, root: Optional[TreeNode]) -> (bool, int):
        if not root:
            return (True, 0)
        
        is_left_balanced, left_h = self.dfs(root.left)
        is_right_balanced, right_h = self.dfs(root.right)

        if not (is_left_balanced and is_right_balanced):
            return (False, 0)

        return (abs(left_h-right_h)<=1, max(left_h, right_h)+1)