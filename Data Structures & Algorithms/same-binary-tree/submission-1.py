# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        q1 = []
        q2 = []

        q1.append(p)
        q2.append(q)

        while len(q1) > 0 and len(q2) > 0:

            a = q1.pop(0)
            b = q2.pop(0)

            if not a and not b:
                continue

        
            if not a or not b:
                return False
                
            if a.val != b.val:
                return False
            
            q1.append(a.left)
            q1.append(a.right)
            q2.append(b.left)
            q2.append(b.right)

        return len(q1) == 0 and len(q2) == 0
