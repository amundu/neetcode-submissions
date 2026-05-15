# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True
        def get_height(root):
            nonlocal is_balanced
            if not root:
                return 0
            
            left_height = get_height(root.left)
            right_height = get_height(root.right)

            if abs(left_height-right_height) > 1:
                is_balanced = False

            return 1 + max(left_height, right_height)

        get_height(root)
        return is_balanced