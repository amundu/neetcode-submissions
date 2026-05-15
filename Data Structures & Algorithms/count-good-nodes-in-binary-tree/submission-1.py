# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.get_good_nodes(root, root.val)
        
    def get_good_nodes(self, root: Optional[TreeNode], path_max: int):
        if not root:
            return 0
        is_good_node = root.val >= path_max
        path_max = max(path_max, root.val)
        children_good_nodes = self.get_good_nodes(root.left, path_max) + self.get_good_nodes(root.right, path_max)
        return children_good_nodes + int(is_good_node)