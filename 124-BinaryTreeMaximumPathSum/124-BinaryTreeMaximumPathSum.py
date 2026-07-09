# Last updated: 7/9/2026, 12:41:26 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = float('-inf')
        def dfs(node):
            nonlocal maxsum
            if node is None:
                return 0 
            
            leftsum  = max(0,dfs(node.left))
            rightsum = max(0,dfs(node.right))
            a = node.val 

            maxsum = max(maxsum, leftsum + rightsum + node.val)
            return node.val + max(leftsum, rightsum)

        dfs(root)
        return maxsum 
        