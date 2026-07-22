# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        store = [(root, root.val)]
        count = 0
        while store:
            node, max_so_far = store.pop(0)
            if node.val >= max_so_far:
                count += 1
            new_max = max(max_so_far, node.val)
            if node.left:
                store.append((node.left, new_max))
            if node.right:
                store.append((node.right, new_max))
        return count