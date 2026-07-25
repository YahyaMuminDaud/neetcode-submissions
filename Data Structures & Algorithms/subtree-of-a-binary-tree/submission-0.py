# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs2(root, root2):
            if root is None and root2 is None:
                return True

            if root is None or root2 is None:
                return False

            if root.val != root2.val:
                return False

            return dfs2(root.left, root2.left) and dfs2(root.right, root2.right)

        def dfs1(root):
            if root is None:
                return False

            if dfs2(root, subRoot):
                return True

            return dfs1(root.left) or dfs1(root.right)

        return dfs1(root)
