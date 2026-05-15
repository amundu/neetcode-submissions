# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        
        def same_tree(t1, t2):
            if not (t1 or t2):
                return True
            if t1 and t2 and t1.val == t2.val:
                return same_tree(t1.left, t2.left) and same_tree(t1.right, t2.right)
            return False
            
        if same_tree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

