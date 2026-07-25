# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        a = []
        q = []

        q.append(root)

        while len(q) > 0:
            rightSide = None
            qLen = len(q)
            for i in range(qLen):
                curr = q.pop(0)
                if curr:
                    rightSide = curr
                    q.append(curr.left)
                    q.append(curr.right)
                    

            if rightSide:
                a.append(rightSide.val)
        
        return a
        