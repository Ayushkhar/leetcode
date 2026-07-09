# Last updated: 7/9/2026, 12:40:24 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p:
            return root
        if root == q:
            return root
        if root is None:
            return None
        
        lefth = self.lowestCommonAncestor(root.left,p,q)
        righth = self.lowestCommonAncestor(root.right,p,q)

        if lefth is None:
            return righth
        if righth is None:
            return lefth
        return root
        