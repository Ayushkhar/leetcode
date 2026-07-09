# Last updated: 7/9/2026, 12:39:39 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isidentical(p,q):
            if p is None and q is None:
                return True 
            if p is None or q is None:
                return False 
            if p.val == q.val:
                return isidentical(p.left, q.left) and isidentical(p.right,q.right)

            return False 
        
  
        def checkSubtree(p, q):
            if p is None:
                return False 
            if q is None:
                return True 
            if isidentical(p,q):
                return True 
            return checkSubtree(p.right, q) or checkSubtree(p.left, q)

        return True if checkSubtree(root, subRoot) else False 



        
        