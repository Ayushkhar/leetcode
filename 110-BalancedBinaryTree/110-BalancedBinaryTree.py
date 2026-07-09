# Last updated: 7/9/2026, 12:41:34 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True  
        def dfs(node):
            nonlocal flag 

            if node is None: 
                return 0 

            lefth = dfs(node.left)
            righth = dfs(node.right)

            if abs(lefth - righth) > 1:
                flag = False   
          
    
            return 1 + max(lefth, righth)
            
        dfs(root)
        return flag 

        